from flask import Blueprint, request, jsonify
from ..models.models import Company
from ..database.db import db

bp = Blueprint('company', __name__, url_prefix='/companies')


@bp.get('/')
def get_companies():
    companies = db.session.execute(db.select(Company)).scalars()
    json_companies = []

    if companies:
        for company in companies:
            json_companies.append(company.as_dict())

    return jsonify(json_companies)


@bp.get('/company/<company_id>')
def get_company(company_id):
    company = db.session.execute(db.select(Company).filter_by(id=company_id)).scalar_one_or_none()
    if company is not None:
        return jsonify(company.as_dict())
    else:
        return jsonify({})


@bp.put('/company/<company_id>')
def update_company(company_id):
    company = db.session.execute(db.select(Company).filter_by(id=company_id)).scalar_one_or_none()

    update_data = request.json
    if company is not None:
        # change
        company.name = update_data.get('name')
        company.description = update_data.get('description')
        company.sigle = update_data.get('sigle')
        company.email = update_data.get('email')

        # persist change
        db.session.commit()
        return jsonify(company.as_dict())
    else:
        return jsonify({})


@bp.post('/company')
def store_company():
    company_data = request.json
    name = company_data.get('name')
    description = company_data.get('description')
    sigle = company_data.get('sigle')
    email = company_data.get('email')

    company = Company(name=name, description=description, sigle=sigle, email=email)

    db.session.add(company)
    db.session.commit()

    return company.as_dict()


@bp.delete('/company/<company_id>')
def delete_company(company_id):
    company = db.session.execute(db.select(Company).filter_by(id=company_id)).scalar_one_or_none()

    if company is not None:
        db.session.delete(company)
        db.session.commit()
        return jsonify({"message": "company deleted"})
    else:
        return jsonify({"message": "company doesn't exist"})
