from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity,unset_jwt_cookies
from werkzeug.security import generate_password_hash, check_password_hash
from application.models import User,Blog,Admin
from application.database import db
from datetime import timedelta,datetime


blog_blueprint=Blueprint("blog",__name__)