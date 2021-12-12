from flask import Flask

from login_test.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from login_test.models import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    from login_test.blueprints.routes import views
    from login_test.blueprints.auth import auth
    app.register_blueprint(views)
    app.register_blueprint(auth)

    from login_test.models import login
    login.init_app(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
