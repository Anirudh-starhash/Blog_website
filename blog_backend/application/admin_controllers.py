from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity,unset_jwt_cookies
from werkzeug.security import generate_password_hash, check_password_hash
from application.models import Admin,User,Blog
from application.database import db
from datetime import timedelta

admin_blueprint=Blueprint("admin",__name__)


    
@admin_blueprint.route("/admin_login",methods=['GET','POST'])
def admin_login():
    if request.method=="POST":
        data=request.get_json()
        email=data.get("email")
        password=data.get("password")
        
        admin=db.session.execute(db.select(Admin).where(Admin.admin_email==email)).scalar()
        if admin is None:
            return jsonify({
                'message':'Incorrect Credentials Librarian Does\'nt exist with this email id', 
            }),201
        
        if admin.password!=password:
            return jsonify({
                'message':'Wrong Password!', 
            }),202
        
        access_token=create_access_token(identity=admin.librarian_id,expires_delta=timedelta(days=1))
        info={
            'id':admin.admin_id,
            'email':admin.admin_email,
            'role':'admin'
        }
        
        return jsonify({
            'access_token':access_token,
            'info':info,
        }),200
        
        
@admin_blueprint.route("/admin_logout",methods=['GET','POST'])
@jwt_required()
def admin_logout():
    if request.method=="POST":
        response=jsonify({
            'message':'Logged out Successfully'
        })
        
        unset_jwt_cookies(response)
        return response,200
    
@admin_blueprint.route("/admin_check_permission",methods=['GET','POST'])
@jwt_required()

def is_permitted():
    admin_identity=get_jwt_identity()
    admin=Admin.query.get(admin_identity)
    print(admin)
    
    
    if admin:
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
        