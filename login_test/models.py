from flask_login import LoginManager
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash


db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'


class User(UserMixin, db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return (
            f'{type(self).__name__}('
            f'id={self.id}, '
            f'username={self.username}, '
            f'email={self.email}, '
            f'password_hash={"**" if self.password_hash is not None else None}'
            ')'
        )

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
