from flask import Blueprint, request, jsonify
from ..models.models import Product
from ..database.db import db

bp = Blueprint('product', __name__, url_prefix='/products')


@bp.get('/')
def get_products():
    products = db.session.execute(db.select(Product)).scalars()
    json_products = []

    if products:
        for product in products:
            json_products.append(product.as_dict())

    return jsonify(json_products)


@bp.get('/product/<product_id>')
def get_product(product_id):
    product = db.session.execute(db.select(Product).filter_by(id=product_id)).scalar_one_or_none()
    if product is not None:
        return jsonify(product.as_dict())
    else:
        return jsonify({})


@bp.put('/product/<product_id>')
def update_product(product_id):
    product = db.session.execute(db.select(Product).filter_by(id=product_id)).scalar_one_or_none()

    update_data = request.json
    if product is not None:
        # change
        product.name = update_data.get('name')
        product.price = update_data.get('price')
        product.description = update_data.get('description')

        # persist change
        db.session.commit()
        return jsonify(product.as_dict())
    else:
        return jsonify({})


@bp.post('/product')
def store_product():
    product_data = request.json
    name = product_data.get('name')
    description = product_data.get('description')
    price = product_data.get('sigle')

    product = Product(name=name, description=description, price=price)

    db.session.add(Product)
    db.session.commit()

    return product.as_dict()


@bp.delete('/product/<product_id>')
def delete_client(product_id):
    product = db.session.execute(db.select(Product).filter_by(id=product_id)).scalar_one_or_none()
    if product is not None:
        db.session.delete(product)
        db.session.commit()

        return jsonify({"message": "product deleted"})
    else:
        return jsonify({"message": "product doesn't exist"})
