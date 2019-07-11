from apis.student.models import Student
from apis.student.schema import student_schema


class StudentDao(object):
    @staticmethod
    def get(student_id):
        result = Student.query.filter_by(id=student_id)
        return student_schema.jsonify(result, many=True)

