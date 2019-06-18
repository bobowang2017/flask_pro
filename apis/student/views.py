import json

from flask import request
from flask_restful import Resource
from apis.student.models import Student, Teacher
from apis.student.schema import student_schema


class StudentView(Resource):

    def get(self):
        print(request.args)
        data = Student.query.join(Teacher, Student.teacher_id == Teacher.id).all()
        res = student_schema.dump(data, many=True)
        return json.dumps({'code': 0, 'msg': res.data})

    def delete(self):
        params = request.args
        student_id = params.get('student_id')
        if not student_id:
            raise Exception("StudentId Is None")
        Student.query.filter_by(id=student_id).delete()
        return json.dumps({'code': 0, 'msg': 'success'})
