from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql
from datetime import datetime
from flask_restful import Api
from flask_migrate import Migrate
from flask_wtf import CSRFProtect #保护
pymysql.install_as_MySQLdb()
app=Flask(__name__)
#学习sqlalchemy
BASE_DIR=os.path.abspath(os.path.dirname(__file__))#当前文件 项目所在的根目录

app.config.from_pyfile('settings.py')
app.config.from_object('settings.TestConfig')
#在Config中使用session
# app.secret_key('dadawdaswd')
db=SQLAlchemy(app) #绑定flsk项目
#负责收集 路由 类视图的注册信息
api=Api(app)
migrate = Migrate(app,db) #数据库管理插件

csrf=CSRFProtect(app) #使用scrf保护