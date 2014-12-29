#-*- coding: utf-8 -*-

from share.framework.bottle import MethodView, view
from apollo.models import UserModel


class ProfileView(MethodView):
    @view('i.html')
    def get(self, ukey):
        user = UserModel.query.get(ukey)
        return user.as_dict()
