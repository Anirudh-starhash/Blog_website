from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity,unset_jwt_cookies
from werkzeug.security import generate_password_hash, check_password_hash
from application.models import User,Blog,Admin
from application.database import db
from datetime import timedelta,datetime

user_blueprint=Blueprint("user",__name__)

@user_blueprint.route("/user_register",methods=['GET','POST'])
def user_register():
    if request.method=="POST":
        data=request.get_json()
        email=data.get("email")
        password=data.get("password")
        name=data.get("name")
        profile_pic=data.get("profile_pic")
        
        hashed_password=generate_password_hash(password,method='pbkdf2:sha256',salt_length=8)
        
        u=db.session.execute(db.select(User).where(User.user_email==email)).scalar()
        # print(u.user_email)
        
        if u is None:
            # means a new user
            
            new_user=User(user_email=email,
                          password=hashed_password,
                          user_name=name,
                          profile_pic=profile_pic)
            db.session.add(new_user)
            db.session.commit()
            
            return jsonify({
                'msg':'Registered Successful!'
            }),200
        
        else:
            return jsonify({
                'msg':'Oops! You are already registered go to login page!'
            }),201
        
        
    
@user_blueprint.route("/user_login",methods=['GET','POST'])
def user_login():
    if request.method=="POST":
        data=request.get_json()
        email=data.get("email")
        password=data.get("password")
        
        u=db.session.execute(db.select(User).where(User.user_email==email)).scalar()
        if u is None:
            return jsonify({
                'message':'Incorrect Credentials User Does\'nt exist with this email id', 
            }),201
        
        if not check_password_hash(u.password,password):
            return jsonify({
                'message':'Wrong Password!', 
            }),202
        
        access_token=create_access_token(identity=u.user_id,expires_delta=timedelta(days=1))
        info={
            'id':u.user_id,
            'email':u.user_email,
            'name':u.user_name,
            'role':'user'
        }
        
        return jsonify({
            'access_token':access_token,
            'info':info,
        }),200
        
        
@user_blueprint.route("/user_logout",methods=['GET','POST'])
@jwt_required()

def user_logout():
    if request.method=="POST":
        response=jsonify({
            'message':'Logged out Successfully'
        })
        
        unset_jwt_cookies(response)
        return response,200
    

@user_blueprint.route("/user_check_permission",methods=['GET','POST'])
@jwt_required()

def is_permitted():
    user_identity=get_jwt_identity()
    user=User.query.get(user_identity)
    
    if user:
        response= jsonify({
            'msg':'Access Granted'
        })
        unset_jwt_cookies(response)
        return response,200
    
    else:
        response= jsonify({
            'msg':'Access Denied'
        })
        unset_jwt_cookies(response)
        return response,201