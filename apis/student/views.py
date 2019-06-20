from flask import request, jsonify
from flask_restful import Resource
from celery.result import AsyncResult
from apis.student.models import Student, Teacher
from apis.student.tasks import my_background_task
from exts import db


class StudentView(Resource):

    def get(self):
        print(request.args)
        # 这种方式返回的只有Student对象
        # data = Student.query.join(Teacher, Student.teacher_id == Teacher.id).add_entity(Teacher).all()
        # 这种方式返回的只有Teacher.name, Student.name字段
        # data = db.session.query(Teacher.name, Student.name).join(Teacher, Student.teacher_id == Teacher.id).all()
        # 这种方式返回的是指定的字段，不过是列表元组的形式返回
        data = db.session.query(Teacher, Student).join(Teacher, Student.teacher_id == Teacher.id).with_entities(
            Teacher.name, Teacher.sex, Student.id, Student.name, Student.sex, Student.birthday).all()
        res = [dict(zip(('tname', 'tsex', 'sid', 'sname', 'ssex', 'sbir'), _d)) for _d in data]
        return jsonify({'code': 0, 'msg': res})
        # return json.dumps({'code': 0, 'msg': res}, ensure_ascii=False)

    def delete(self):
        params = request.args
        student_id = params.get('student_id')
        if not student_id:
            raise Exception("StudentId Is None")
        Student.query.filter_by(id=student_id).delete()
        db.session.commit()
        return jsonify({'code': 0, 'msg': 'success'})


class CeleryTaskView(Resource):
    def get(self):
        my_background_task.apply_async((4, 5))
        return jsonify({'code': 0, 'msg': 'success'})


class CeleryTaskResultView(Resource):
    def get(self):
        res = AsyncResult("bff19ef2-fcad-4b85-9792-6d56184020e9")
        return jsonify({'code': 0, 'msg': res.result})
