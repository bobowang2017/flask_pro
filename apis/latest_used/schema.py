# -*- coding: utf-8 -*-
from app import ma


class ProjectSchema(ma.Schema):
    class Meta:
        fields = ("id", "code", "name", "description", "created_time", "updated_time")


class ApplicationSchema(ma.Schema):
    class Meta:
        fields = ("id", "app_name", "pro_id", "created_time", "updated_time", "project")

    project = ma.Nested(ProjectSchema)

    # links = ma.Hyperlinks({
    #     'self': ma.URLFor('book_detail', id='<id>'),
    #     'collection': ma.URLFor('book_list')
    # })


app_schema = ApplicationSchema()
pro_schema = ProjectSchema()
