from server.store.gino import db


class AdminUser(db.Model):
    __tablename__ = "admin_user"

    id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer(), unique=True, nullable=False)
    username = db.Column(db.Text(), nullable=False)
    password = db.Column(db.String(256), nullable=False, unique=True)
