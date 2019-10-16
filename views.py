from flask import Flask
from flask import render_template,redirect,request
from model import *
from test import MyData
from settings import *
import functools
from flask import session
# session['key'] = 'value'
# app=Flask(__name__)
from main import app
import hashlib
def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result
def LoginValid(fun):
    @functools.wraps(fun)
    def inner(*args,**kwargs):
        user_id=request.cookies.get("user_id")
        email = request.cookies.get("email")
        session_email = session.get('email')
        print(session_email)
        # session_email = session.get('email')
        # print(session_email)
        if user_id and email:
            user = User.query.filter(User.email==email,User.id==user_id).first()
            if user:
                return fun(*args,**kwargs)
            else:
                return redirect('/login/')
        else:
            return redirect("/login/")
    return inner

@app.route("/base/")
def base():
    return render_template('base.html')



@app.route("/index/")
@LoginValid
def index():
    # userinfo = UserInfo(name='python',age=19)
    # userinfo.save()
    data = UserInfo.query.get(4)

    return render_template('index.html',**locals())
@app.route("/userinfo/")
@LoginValid
def userinfo():
    #获取当前的的年，月
    obj=MyData()
    result =obj.get_date()
    return render_template('userinfo.html',**locals())

@app.route("/login/",methods=['post','get'])
def login():
    error=''
    if request.method == "POST":
        email=request.form.get("email")
        password = request.form.get("password")

        if email and password:

            user = User.query.filter(User.email == email,User.password == setPassword(password)).first()
            if user is not None:
                response = redirect("/index/")
                response.set_cookie("email",user.email)
                response.set_cookie("user_id",str(user.id))
                session["email"] = user.email
                return response
                # return redirect('/index/')
            else:
                error="邮箱密码不正确"
        else:
            return '参数不能为空'
    return render_template('login.html',error=error)

# @app.route("/register/",methods=['post','get'])
# def register():
#     if request.method=="POST":
#         ##注册
#         email = request.form.get("email")
#         password = request.form.get("password")
#         data = User.query.filter(User.email == email).first()
#         if data:
#             ##存在
#             return redirect("/login/")
#         user=User(email=email,password=password)
#         user.save()
#     # return render_template('register.html')
#     return '注册成功'

@app.route("/register/",methods=['post','get'])
def register():
    error= ""
    if request.method=="POST":
        ##注册
        name=request.form.get('name')
        email = request.form.get("email")
        password = request.form.get("password")
        if email and password:
            user = User.query.filter(User.email == email).first()
            if user:
               error = "邮箱已存在"
            else:
                user = User()
                user.email = email
                user.password = setPassword(password)
                user.save()
                return redirect("/login/")
        else:
            error = "参数不能为空"
    return render_template('register.html',error=error)
    # return '注册成功'






@app.route("/perfect/infomation/",methods=['post','get'])

def perfect_infomation():

    if request.method=="POST":
        ##注册
        user_id = request.form.get("id")
        # photo=request.files
        #获取图片的 名字 内容 保存图片
        ## 数据库中 图片路径
        photo = request.files.get('photo')

        # methon = [one for one in dir(data) if not one.startswith("_")]
        # print(methon)
        # print(data.filename) #图片名字
        # print(data.content_length) #图片长度
        # print(data.content_type) #文件类型
        # print(data.headers) #图片头部
        # print(data.mimetype) #内容类型
        # print(data.mimetype_params) #类型参数
        # print(data.name) ##字段名字
        # print(data)

        user = User.query.filter(User.id == user_id).first()
        if user:
            ## 保存图片
            #将有图片存到数据库中
            file_name = photo.filename
            photo_path=os.path.join('img',file_name)
            path = os.path.join(STATIC_PATH,photo_path)
            print(photo_path)
            #将图片路径存在数据库中
            photo.save(path)
            user.photo = photo_path
            user.merge()
        else:
            return "用户不存在"
    user = User.query.filter(User.id==1).first()
    photo = user.photo
    return render_template('photo.html',**locals())
    # return '增加成功'

@app.route("/logout/",methods=['post','get'])
def logout():
    # cookie = request.cookies('user_id')
    # print(cookie)
    req=redirect("/login/")
    req.delete_cookie("email")
    req.delete_cookie('user_id')
    session.pop("email")
    # del session["email"]
    return req

@app.route('/testget/')
def testget():
    # name=request.args.get('name',None)
    name=request.form.get('name',None)
    print(name)
    return render_template('testget.html')

@app.route('/leave_list/',methods=['post','get'])
@LoginValid
def leave_list():
    # name=request.args.get('name')
    if request.method=="POST":
        user_id = request.cookies.get("user_id")

        data=request.form
        #保存数据
        leave = Leave()

        leave.request_id=int(user_id)  # 请求id
        leave.request_name = data.get("username")  # 请求姓名
        leave.request_type = data.get("type")  # 请假类型
        leave.request_start = data.get("start_time")  # 请假开始时间
        leave.request_end = data.get("end_time")  # 请假的结束时间
        leave.request_number = data.get("day")  # 请假的结束时间
        leave.request_description = data.get("dec")  # 请假描述
        leave.request_phone = data.get("phone")  # 联系人的手机号
        leave.request_status = 0  # 请假状态
        print(data)
        leave.save()
    return render_template('leave_list.html')
from sdk.pager import Pager
@app.route('/leave_all_list/<int:page>',methods=['post','get'])
@LoginValid
def leave_all_list(page):
    leave = Leave.query.filter(Leave.request_id == request.cookies.get("user_id")).all()
    pager = Pager(leave,10)
    page_data = pager.page_data(page)
    return render_template('leave_all_list.html',**locals())


from flask import jsonify
@app.route("/chexiao/",methods=['get','post'])
def chexiao():
    id = request.form.get("id")

    leave = Leave.query.filter(Leave.id==id).first()
    leave.delete()

    result = {"code":1000,'msg':"删除成功"}
    return jsonify(result)


from form import TaskForm
@app.route("/add_task/",methods=['get','post'])
def add_task():
    task = TaskForm()
    #     print(dir(task))
    # print("task.csrf_token%s"%task.csrf_token) ##csrf_token
    # print("task.errors%s"%task.errors)  ###错误
    # print("task.validate%s"%task.validate) ###判断是否是一个合法请求
    # print("task.validate_on_submit%s"%task.validate_on_submit) ##判断是否是一个有效的post 请求
    # print("task.data%s"%task.data)   ##请求的数据

    error={}
    if request.method=="POST":
        if task.validate_on_submit():
            pass
            # 获取数据
            FromData = task.data
            #保存数据 数据库当中 建立模型
        else:
            error = task.errors
            print(error)


    print(error)

    return render_template('add_task.html',**locals())
if __name__ == '__main__':

    app.run(debug=True)