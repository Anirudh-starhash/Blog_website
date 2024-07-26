from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity,unset_jwt_cookies
from werkzeug.security import generate_password_hash, check_password_hash
from application.models import User,Blog,Admin
from application.database import db
from datetime import timedelta,datetime
import requests

blog_blueprint=Blueprint("blog",__name__)

@blog_blueprint.route("/getInfo/<int:id>" ,methods=['GET','POST'])
def getInfo(id):
    blog_url="https://api.npoint.io/c790b4d5cab58020d391"
    response=requests.get(blog_url)
    all_data=response.json()
    
    blogs=db.session.execute(db.Select(Blog).where(Blog.blog_id==id)).scalars().all()
    return jsonify({
        'blogs':all_data,
        'my_blogs':blogs
    }),200
    
@blog_blueprint.route("/getInfoBlog/<int:id>",methods=['GET','POST'])
def getBlog(id):
    blog_url="https://api.npoint.io/c790b4d5cab58020d391"
    response=requests.get(blog_url)
    all_data=response.json()
    req_blog=[blog for blog in all_data if blog["id"]==id]
    
    return jsonify({
        'blog':req_blog[0]
    })
    
