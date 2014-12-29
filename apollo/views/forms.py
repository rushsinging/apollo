#-*- coding: utf-8 -*-


from wtforms import Form, fields, validators


class UserSettingForm(Form):
    nickname = fields.StringField(
        u'昵称',
        validators=[validators.required(), validators.length(max=32)]
    )
    title = fields.StringField(
        u'签名',
        validators=[validators.required(), validators.length(max=128)]
    )
    summary = fields.TextAreaField(
        u'简介',
        validators=[validators.required(), validators.length(max=256)]
    )
    birthday = fields.DateField()
    gender = fields.RadioField(
        u'性别',
        validators=[validators.required()],
        choices=[(u'male', u'男'), (u'female', u'女')]
    )
