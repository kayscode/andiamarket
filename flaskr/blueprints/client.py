from flask import Blueprint, request, jsonify
from ..models.models import Client
from ..database.db import db

bp = Blueprint('client', __name__, url_prefix='/clients')


# get all existing product
@bp.get('/')
def get_clients():
    clients = db.session.execute(db.select(Client)).scalars()
    json_clients = []

    if clients:
        for client in clients:
            json_clients.append(client.as_dict())

    return jsonify(json_clients)


@bp.get('/client/<client_id>')
def get_client(client_id):
    user = db.session.execute(db.select(Client).filter_by(id=client_id)).scalar_one_or_none()
    if user is not None:
        return jsonify(user.as_dict())
    else:
        return jsonify({})


@bp.put('/client/<client_id>')
def update_client(client_id):
    user = db.session.execute(db.select(Client).filter_by(id=client_id)).scalar_one_or_none()

    update_data = request.json
    if user is not None:
        # change
        user.first_name = update_data.get('first_name')
        user.last_name = update_data.get('last_name')
        user.middle_name = update_data.get('middle_name')
        user.email = update_data.get('email')
        user.phone_number = update_data.get('phone_number')

        # persist change
        db.session.commit()
        return jsonify(user.as_dict())
    else:
        return jsonify({})


@bp.post('/client')
def store_client():
    user_data = request.json
    first_name = user_data.get('first_name')
    middle_name = user_data.get('middle_name')
    last_name = user_data.get('last_name')
    phone_number = user_data.get('phone_number')
    email = user_data.get('email')

    client = Client(first_name=first_name, middle_name=middle_name, last_name=last_name, email=email,
                    phone_number=phone_number)

    db.session.add(client)
    db.session.commit()

    return user_data


@bp.delete('/client/<client_id>')
def delete_client(client_id):
    user = db.session.execute(db.select(Client).filter_by(id=client_id)).scalar_one_or_none()
    if user is not None:
        db.session.delete(user)
        db.session.commit()

        return jsonify({"message": "user deleted"})
    else:
        return jsonify({"message": "user doesn't exist"})
