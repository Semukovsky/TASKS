from flask import Flask, jsonify, Blueprint, request
from sqlalchemy import or_

from data import db_session
from data.users import User


app = Flask(__name__)
blueprint = Blueprint('users_api', __name__, template_folder="templates")


@blueprint.route('/api/users/', methods=['GET'])
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    users_json = [
        {
            "id": user.id,
            "surname": user.surname,
            "name": user.name,
            "email": user.email,
        }
        for user in users
    ]

    return jsonify(users_json)

@blueprint.route('/api/users/<int:id>/', methods=['GET'])
def get_user(id):
    db_sess = db_session.create_session()
    if not isinstance(id, int):
        return jsonify({
            "error": "Invalid type of id"
        })
    user = db_sess.query(User).get(id)
    if user is None:
        return jsonify({
            "error": "Not found"
        })
    return jsonify({
        "id": user.id,
        "surname": user.surname,
        "name": user.name,
        "email": user.email,
    })

@blueprint.route('/api/users/', methods=['POST'])
def create_user():
    db_sess = db_session.create_session()
    data = request.json
    if not data:
        return jsonify({"error": "No data"})
    if not data.get('name') or not data.get('email'):
        print(data)
        return jsonify({"error": "Invalid data"})
    if db_sess.query(User).filter(or_(User.id == data['id'], User.email == data['email'])).first():
        return jsonify({"error": "User already exists"})
    user = User()
    user.id = data.get('id')
    user.surname = data.get('surname')
    user.name = data.get('name')
    user.age = data.get('age')
    user.position = data.get('position')
    user.speciality = data.get('speciality')
    user.email = data.get('email')
    db_sess.add(user)
    db_sess.commit()
    return jsonify({"success": "OK"})

@blueprint.route('/api/users/<int:id>/', methods=['DELETE'])
def delete_user(id):
    db_sess = db_session.create_session()
    if not isinstance(id, int):
        return jsonify({
            "error": "Invalid type of id"
        })
    user = db_sess.query(User).get(id)
    if user is None:
        return jsonify({
            "error": "Not found"
        })
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({"success": "OK"})

@blueprint.route('/api/users/<int:id>/', methods=['PUT'])
def update_user(id):
    db_sess = db_session.create_session()
    if not isinstance(id, int):
        return jsonify({
            "error": "Invalid type of id"
        })
    user = db_sess.query(User).get(id)
    if user is None:
        return jsonify({
            "error": "Not found"
        })
    data = request.json
    if not data:
        return jsonify({"error": "No data"})
    user.id = data.get('id', user.id)
    user.surname = data.get('surname', user.surname)
    user.name = data.get('name', user.name)
    user.age = data.get('age', user.age)
    user.position = data.get('position', user.position)
    user.speciality = data.get('speciality', user.speciality)
    user.email = data.get('email', user.email)
    db_sess.add(user)
    db_sess.commit()
    return jsonify({"success": "OK"})



if __name__ == "__main__":
    db_session.global_init("db/mars_explorer.db")
    app.register_blueprint(blueprint)
    app.run(port=8080, host="127.0.0.1")