
from marshmallow import Schema, fields

class Publication():
    def __init__(self, abstract, title):
        self.abstract = abstract
        self.title = title

    def __repr__(self):
        return '<Publication(title={self.title!r}>'.format(self=self)

class PublicationSchema(Schema):
    abstract = fields.Str()
    title = fields.Str()