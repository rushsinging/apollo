#-*- coding: utf-8 -*-

from share.framework.bottle import APIBlueprint

from .user import UserAPI

bp_apis = APIBlueprint('apis')
UserAPI.attach_to(bp_apis)
