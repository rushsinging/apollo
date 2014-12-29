#-*- coding: utf-8 -*-

from share.framework.bottle.restful import RESTfulBackendAPI
from share.framework.bottle.engines import db
from share.framework.bottle.restful import resful_validator
from share.utils.decorators import authorization_required

from apollo.models import UserModel
from . import forms


class UserBackendAPI(RESTfulBackendAPI):
    path = '/user'
    methods = ['GET', 'POST']

    @authorization_required
    @resful_validator(forms.ukey)
    def get(self, ukey):
        user = UserModel.query.get(ukey)
        if not user:
            return {}
        return user.as_dict()

    @resful_validator(forms.ukey, forms.nickname)
    @authorization_required
    def create(self, ukey, nickname):
        user = UserModel(
            ukey=ukey, nickname=nickname,
            avatar='', gender='male', title='', summary='',
        )
        db.session.add(user)
        db.session.commit()
        return user.as_dict()
