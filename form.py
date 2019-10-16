import wtforms
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms import ValidationError

def keywords_valid(form,field):
    """
    判断填写的数据是否有敏感字
    这个字段 不需要手动传参
    :param form: 表单
    :param field: 字段
    :return:
    """
    data = field.data
    keywords = ['我靠','nicai','台湾']
    if data in keywords:
        raise ValidationError("不可以,是这个敏感词汇")
class TaskForm(FlaskForm):
    # name = wtforms.StringField(label="任务名字")
    # description = wtforms.TextField(label="任务描述")
    # time = wtforms.DateField(label="任务时间")
    # pubilc = wtforms.StringField(label="任务的发布人")
    name = wtforms.StringField(
        render_kw={
            "class": 'form-control',
            "placeholder":"任务名字"
        },
        validators = [
            validators.DataRequired('任务中名字不能为空'),
            # validators.Email("必须符合邮箱的格式")
            keywords_valid
    ]
    )
    description = wtforms.TextField(
        render_kw={
            "class": 'form-control',
            "placeholder": "任务的描述"
        },
        validators=[
            # validators.EqualTo("name") #字段必须和name一样
        ]

    )
    time = wtforms.DateField(
        render_kw={
            "class": 'form-control',
            "placeholder": "任务的时间"
        }
    )
    pubilc = wtforms.StringField(
        render_kw={
            "class": 'form-control',
            "placeholder": "任务的发布"
        }
    )
