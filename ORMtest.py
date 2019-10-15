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
# app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(BASE_DIR,'test.db') #链接sqlist3配置
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/flask'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_RATACK_MODIFICATIONS']=True
app.config['DEBUG']=True

db=SQLAlchemy(app) #绑定flsk项目
#创建模型
class BaseModel(db.Model):
    __abstract__=True
    id=db.Column(db.Integer,primary_key=True)
    def save(self):
        db.session.add(self)
        db.session.commit()
    def merge(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class UserInfo(BaseModel):
    __tablename__='userinfo'
    name =db.Column(db.String(32))
    time = db.Column(db.DATETIME,default=datetime.now())
    age =db.Column(db.Integer)
auto_now = True
class User(BaseModel):
    __tablename__='user'
    name =db.Column(db.String(32))
    phone = db.Column(db.String(11))
# 数据迁移
db.create_all()
#增加
# userinfo = UserInfo(name='laowang',age=19)
# db.session.add(userinfo)
# db.session.commit()

# db.session.add_all([
#     UserInfo(name='laowang',age=20),
#     UserInfo(name='laowang',age=20),
#     UserInfo(name='laowang',age=20),
#     UserInfo(name='laowang',age=20),
# ])
# db.session.commit()
#查询
# all
# data=UserInfo.query.all()
# print(data)
# get
# data=UserInfo.query.get(1)
# print(data)
# print(data.name)

# filter
# data=UserInfo.query.filter_by(name='laowang').all()
# print(data)

# data=UserInfo.query.filter(UserInfo.name=='laowang').all()
# print(data)

# get
# data=UserInfo.query.get(ident=1)
# print(data)
# print(data.name)

# first
# data=UserInfo.query.first()
# print(data)

# order_by

#升序
# data=UserInfo.query.order_by(UserInfo.id).all()
# print(data)
# data=UserInfo.query.order_by("id").all()
# print(data)
#降序
# ss=UserInfo.query.order_by(UserInfo.id.desc()).all()
# print(ss)
# ss=UserInfo.query.order_by(db.desc('id')).all()
# print(ss)

#分页
# data= UserInfo.query.offset(2).limit(2).all()
# print(data)

#修改
# data=UserInfo.query.filter(UserInfo.id==1).first()
# # data.name='lisi'
# # db.session.merge(data)
# # db.session.commit()

#删除
# data=UserInfo.query.filter(UserInfo.id==1).first()
# db.session.delete(data)
# db.session.commit()


#增加
# userinfo=UserInfo(name='wuwu',age=10)
# userinfo.save()
#更新数据
# userinfo=UserInfo.query.get(8)
# userinfo.name='aliu'
# userinfo.merge()

#删除数据
userinfo= UserInfo.query.get(7)
userinfo.delete()
@app.route("/")
def index():
    return "ORM测试"
if __name__ == '__main__':
    app.run()