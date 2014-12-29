#-*- coding: utf-8 -*-

from share.framework.bottle import BackendsBlueprint

bp_backends = BackendsBlueprint('backends')

from .user import UserBackendAPI
UserBackendAPI.attach_to(bp_backends)
