from flask import Blueprint, jsonify, request
from application.app import db
from application.models.userModel import User

# create the blueprint
demo_api_blueprint = Blueprint('demo_api', __name__, url_prefix='/api')


@demo_api_blueprint.route("/<string:name>")
def demo_api(name):
    user = User(name)
    db.session.add(user)
    db.session.commit()
    return jsonify({"name": user.name, "id": user.id})


@demo_api_blueprint.route("/showAll", methods=['GET'])
def show_all():
    query = db.session.query(User).all()

    people = []
    for p in query:
        person = dict()
        person["name"] = p.name
        person["id"] = p.id
        people.append(person)

    return jsonify({"people": people})
