from app import app, db
from flask import request, jsonify
from app.models import User


@app.route('/api/', methods=['GET', 'POST'])
def api():
    email = request.args.get('email')
    password = request.args.get('password')

    user = User.query.filter_by(email=email).first()

    # if user doesn't exist, reload page and flash message
    if user is None or not user.check_password(password):
        return jsonify({ 'error': 'Incorrect Credentials' })


    return jsonify(user)
