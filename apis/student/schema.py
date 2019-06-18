# -*- coding: utf-8 -*-
from exts import ma


class TeacherSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "password", "sex", "birthday")


class StudentSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "teacher_id", "sex", "birthday")


teacher_schema = TeacherSchema()
student_schema = StudentSchema()
