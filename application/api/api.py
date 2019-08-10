from flask import Blueprint, jsonify, request
from application.app import db
from application.models.userModel import User

# create the blueprint
api_blueprint = Blueprint('api', __name__)


@api_blueprint.route("/users", methods=['GET'])
def get_users():
    """Get all the users from the database"""
    query = User.query.all()

    people = []
    for p in query:
        person = dict()
        person["name"] = p.name
        person["id"] = p.id
        people.append(person)

    return jsonify({"people": people})


@api_blueprint.route("/users/<value>", methods=['GET'])
def get_user(value):
    """get a single user from the database either by user id or name"""
    try:
        i = int(value)
        query = User.query.get(i)
    except ValueError:
        query = User.query.filter_by(name=value).first()

    if not query:
        return jsonify({"message": "{}, is not in the database".format(value)})

    return jsonify({query.id: query.name})


@api_blueprint.route("/users/<string:name>", methods=['POST'])
def add_user(name):
    """ add a new user to the database"""
    user = User(name)
    db.session.add(user)
    db.session.commit()
    return jsonify({"name": user.name, "id": user.id})


@api_blueprint.route("/users/<int:id>", methods=['PUT'])
def update_user(id):
    """update the user, can only input id"""
    query = User.query.get(id)

    if not query:
        return jsonify({"message": "user id: {}, is not in the system".format(id)})

    query.name = request.json["name"]
    query.id = request.json["id"]
    db.session.add(query)
    db.session.commit()
    return jsonify({"updated user": {query.id: query.name}})


@api_blueprint.route("/users/<int:id>", methods=['DELETE'])
def delete_user(id):
    """delete the user from the database"""
    query = User.query.get(id)

    if not query:
        return jsonify({"message": "user id: {}, is not in the system".format(id)})

    db.session.delete(query)
    db.session.commit()
    return jsonify({"message": "user id: {} has been deleted!".format(id)})

