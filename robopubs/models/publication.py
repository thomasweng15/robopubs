
from marshmallow import Schema, fields

class Publication():
    def __init__(self, id, abstract, title):
        self.id = id
        self.abstract = abstract
        self.title = title

    def __repr__(self):
        return '<Publication(title={self.title!r}>'.format(self=self)

class PublicationSchema(Schema):
    id = fields.Str()
    abstract = fields.Str()
    title = fields.Str()