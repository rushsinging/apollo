#-*- coding: utf-8 -*-

from share.framework.bottle import MethodView, view


class HomeView(MethodView):
    @view('home.html')
    def get(self):
        return {}


class AboutView(MethodView):
    @view('about.html')
    def get(self):
        return {}
