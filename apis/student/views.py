import json

from flask import request, jsonify
from flask_restful import Resource
from celery.result import AsyncResult

from apis.student.dao import StudentDao
from apis.student.models import Student, Teacher
from apis.student.tasks import my_background_task
from exts import db


class StudentView(Resource):

    def get(self):
        print(request.args)
        # result = StudentDao.get(1)
        # return result
        # 这种方式返回的只有Student对象
        data = Student.query.join(Teacher, Student.teacher_id == Teacher.id).add_entity(Teacher).all()
        print(data)
        # 这种方式返回的是指定的字段，不过是列表元组的形式返回
        # query = db.session.query(Teacher).join(Student, Student.teacher_id == Teacher.id).with_entities(
        #     Teacher.name, Teacher.sex, Student.id, Student.name, Student.sex, Student.birthday)
        # 也可以采用下面这种简洁的写法
        query = Teacher.query.join(Student, Student.teacher_id == Teacher.id).with_entities(
            Teacher.name, Teacher.sex, Student.id, Student.name, Student.sex, Student.birthday)
        data = query.all()
        return json.dumps({'code': 0, 'msg': data}, ensure_ascii=False)
        # desc = query.column_descriptions
        # print(desc)
        # res = [dict(zip(('tname', 'tsex', 'sid', 'sname', 'ssex', 'sbir'), _d)) for _d in data]
        # return jsonify({'code': 0, 'msg': res})
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
        # key = "celery-task-meta-"+"f988b061-8b57-4d3f-a678-d17ae79e1f54"
        # result = redis_cli.get_instance(key)
        res = AsyncResult("f988b061-8b57-4d3f-a678-d17ae79e1f54", backend='redis://localhost:6379/1')
        return jsonify({'code': 0, 'msg': res.result})
        # return json.loads(result)
