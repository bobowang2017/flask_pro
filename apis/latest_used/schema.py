# -*- coding: utf-8 -*-
from marshmallow import validates, ValidationError

from app import ma


class ProjectSchema(ma.Schema):
    class Meta:
        fields = ("id", "code", "name", "description", "created_time", "updated_time")


class ApplicationSchema(ma.Schema):
    class Meta:
        fields = ("id", "app_name", "pro_id", "created_time", "updated_time", "project")

    project = ma.Nested(ProjectSchema)

    @validates('pro_id')
    def validate_pro_id(self, value):
        if not value:
            raise ValidationError('pro_id must not be none.')
        if not isinstance(value, int):
            raise ValidationError('pro_id must be integer.')

    @validates('app_name')
    def validate_quantity(self, value):
        if len(value) < 10:
            raise ValidationError('Quantity must be greater than 10.')
        if len(value) > 30:
            raise ValidationError('Quantity must not be greater than 30.')

    # links = ma.Hyperlinks({
    #     'self': ma.URLFor('book_detail', id='<id>'),
    #     'collection': ma.URLFor('book_list')
    # })


app_schema = ApplicationSchema()
pro_schema = ProjectSchema()
