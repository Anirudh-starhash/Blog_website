import os
from flask import Flask
from application.database import db
from application.config import LocalDevelopmentConfig
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from application.user_controllers import *
from application.blog_controllers import *
from application.admin_controllers import *

app=None


def create_app():
    app=Flask(__name__)
    app.register_blueprint(user_blueprint,url_prefix='/api')
    app.register_blueprint(blog_blueprint,url_prefix='/api')
    app.register_blueprint(admin_blueprint,url_prefix='/api')

    if os.getenv('ENV',"development")=="production":
        raise Exception("Currently no os production config is setup")
    else:
        print('Starting local Development')
        
        app.config.from_object(LocalDevelopmentConfig)
        app.config['SECRET_KEY']="Secret is meant to be Secret"
        app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
        db.init_app(app)   
        app.app_context().push()
        return app
    
app=create_app()
CORS(app)
migrate=Migrate(app)
jwt=JWTManager(app)


    
with app.app_context():
    db.create_all()
    





if __name__=="__main__":
    app.run(debug=True)
    
