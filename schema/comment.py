from marshmallow import Schema, fields, validates, ValidationError


class CommentSchemaBase(Schema):
    comment = fields.Str(required=True, allow_none=False)

    @validates("comment")
    def validate_comment(self, value):
        if not value:
            raise ValidationError("Comment shouldn't be empty")


class CommentRequestSchema(CommentSchemaBase):
    pass


class CommentItemResponseSchema(CommentSchemaBase):
    id = fields.Int(required=True, allow_none=False)
    author = fields.Str(required=True, allow_none=False, attribute="author_login")
    timestamp = fields.DateTime(required=True, allow_none=False)
