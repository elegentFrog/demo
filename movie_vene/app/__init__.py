from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
import pymysql
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Hhuc1115@www.elegantfrog.xyz:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = 'af2fad8cfe1f4c5fac4aa5edf6fcc8f3'
app.config["REDIS_URL"] = "redis://www.elegantfrog.xyz:6379/1"
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")
app.config["FC_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/users/")
app.debug = True
db = SQLAlchemy(app)
rd = FlaskRedis(app)

from app.home import home as home_blueprint  #前台
from app.admin import admin as admin_blueprint  #后台

app.register_blueprint(home_blueprint)   #注册蓝图（前台）
app.register_blueprint(admin_blueprint, url_prefix="/admin") #注册蓝图（后台）

@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404