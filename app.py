from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Database configuration (replace with your credentials)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/loginDB'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the app
    db.init_app(app)

    # Simple route to check if the app works
    @app.route('/')
    def hello():
        return "Hello, Flask!"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
