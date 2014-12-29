# -*- coding: utf-8 -*-

from share.framework.bottle.restful import RESTfulOpenAPI
from share.framework.bottle.restful.validator import resful_validator

from apollo.models import UserModel
from . import forms


class UserAPI(RESTfulOpenAPI):
    path = '/oauth2/client'
    methods = ['GET', 'POST', 'PUT']

    @resful_validator(forms.ukey)
    def get(self, ukey):
        user = UserModel.query.get(ukey)
        return user.as_dict() if user else {}

    @resful_validator(forms.ukey)
    def create(self, ukey):
        pass
