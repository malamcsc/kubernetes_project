from app.helper.Constants import Constants
from app import db


# Define a User model
class Users(db.Model):
    __tablename__  = Constants.tbl_alerts
    __table_args__ = {Constants.ORM_ExtendExisting: True}
    id      = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name    = db.Column(db.String(192), nullable=False)
    city  = db.Column(db.String(192), nullable=False)
    salary  = db.Column(db.Integer, nullable=False)
    skill  = db.Column(db.String(192), nullable=False)
    

