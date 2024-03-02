from apifairy import body, response

from core import database
from core.models import Category
from core.schema import CategoryInsertSchema, CategoryResponseSchema

from . import inventory_category_api_blueprint

category_schema_response = CategoryResponseSchema(many=True)
category_schema_insert = CategoryInsertSchema()


@inventory_category_api_blueprint.route("/category", methods=["GET"])
@response(category_schema_response)
def category():
    return Category.query.all()


@inventory_category_api_blueprint.route("/category", methods=["POST"])
@body(category_schema_insert)
@response(category_schema_insert)
def category_insert(kwargs):
    new_category = Category(**kwargs)
    database.session.add(new_category)
    database.session.commit()
    return new_category
