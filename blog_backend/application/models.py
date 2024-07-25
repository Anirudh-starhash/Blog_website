from .database import db

class User(db.Model):
    __tablename__='user'
    user_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_name=db.Column(db.String(128))
    user_email=db.Column(db.String(128))
    password=db.Column(db.String(128))
    profile_pic=db.Column(db.String(128))
    
class Blog(db.Model):
    __tablename__='blog'
    blog_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    blog_name=db.Column(db.String(128))
    blog_content=db.Column(db.String(128))
    
class Admin(db.Model):
    __tablename__='admin'
    admin_id=db.Column(db.VARCHAR,primary_key=True)
    admin_name=db.Column(db.String(128))
    admin_email=db.Column(db.VARCHAR)
    password=db.Column(db.VARCHAR)
    admin_profile_pic=db.Column(db.String(128))
    
    
    