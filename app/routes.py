from app import app, db
from flask import request, jsonify
from app.models import User


@app.route('/')
def index():
    return ''

@app.route('/api/', methods=['GET', 'POST'])
def api():
    email = request.args.get('email')

    user = User.query.filter_by(email=email).first()

    # if user doesn't exist, reload page and flash message
    if user is None:
        return jsonify({ 'error': 'User does not exist' })

    data = []

    data.append({
        'name': user.name,
        'email': user.email
    })

    return jsonify(data)
