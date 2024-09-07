from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/loginDB'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the app
    db.init_app(app)

    @app.route('/')
    def hello():
        return "Hello, Flask!"

    @app.route('/login', methods=['POST'])
    def login():
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # For simplicity, we'll just use hardcoded credentials here
        # You should query the database to verify user credentials
        if username == 'testuser' and password == 'testpassword':
            return jsonify({'success': True})
        else:
            return jsonify({'success': False})

    return app
