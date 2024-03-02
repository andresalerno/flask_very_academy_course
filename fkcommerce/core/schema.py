from core import ma


class CategoryResponseSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    name = ma.String(required=True)
    slug = ma.String(required=True)


class CategoryInsertSchema(ma.Schema):
    name = ma.String(required=True)
    slug = ma.String(required=True)
    is_active = ma.Boolean(required=True)
    parent_id = ma.Integer(allow_none=True)
