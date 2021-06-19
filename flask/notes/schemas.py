from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
import models

class NoteSchema(SQLAlchemySchema):
    class Meta:
        model = models.Note
        load_instance = True

    id = auto_field()
    title = auto_field(required=True)
    body = auto_field()
