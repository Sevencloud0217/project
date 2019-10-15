import functools
def flask_url(func):
    def inner(*args,**kwargs):
        print('url')
        func(*args,**kwargs)
        return inner

def loginouter(func):
    print("我是登入验证码")
    @functools.wraps(func)
    def inner(*arge,**kwargs):
        print("验证")
        func()
    return inner
@flask_url
@loginouter
def index():
    print('index')
print(index.__name__)

# @loginouter
# def userinfo():
#     print('userinfo')
# print(userinfo.__name__)


# print(index.__name__)
# index = loginouter(index)
# index()