#-*- coding: utf-8 -*-

from share.framework.bottle.app import Blueprint

from .home import HomeView, AboutView
from .settings import SettingsView
from .i import ProfileView

blueprint_www = Blueprint('www', subdomain='www')

blueprint_www.add_url_rule(
    '/', view_func=HomeView.as_view(), methods=['GET'],
    endpoint='main'
)

blueprint_www.add_url_rule(
    '/about/', view_func=AboutView.as_view(), methods=['GET'],
    endpoint='about'
)

blueprint_www.add_url_rule(
    '/i/<ukey:uid>/settings/',
    view_func=SettingsView.as_view(), methods=['GET', 'POST'],
    endpoint='settings'
)

blueprint_www.add_url_rule(
    '/i/<ukey:uid>/', view_func=ProfileView.as_view(), methods=['GET'],
    endpoint='profile'
)
