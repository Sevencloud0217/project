from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql
from datetime import datetime
pymysql.install_as_MySQLdb()
app=Flask(__name__)
#学习sqlalchemy
BASE_DIR=os.path.abspath(os.path.dirname(__file__))#当前文件 项目所在的根目录

#链接数据库

app.config.from_pyfile('settings.py')
app.config.from_object('settings.TestConfig')
#在Config中使用session
# app.secret_key('dadawdaswd')
db=SQLAlchemy(app) #绑定flsk项目

