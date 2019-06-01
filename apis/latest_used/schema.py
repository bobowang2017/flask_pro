# -*- coding: utf-8 -*-
from marshmallow import Schema, fields


class ProjectSchema(Schema):
    id = fields.Integer()
    code = fields.Str()
    name = fields.Str()
    description = fields.Str()
    created_time = fields.DateTime()
    updated_time = fields.DateTime()


class ApplicationSchema(Schema):
    id = fields.Integer()
    app_name = fields.Str()
    pro_id = fields.Integer()
    created_time = fields.DateTime()
    updated_time = fields.DateTime()
