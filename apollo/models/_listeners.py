# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from sqlalchemy import event

from share.framework.bottle.engines import db
from share.framework.bottle.user import reload_user_meta

from .user import UserModel


# 下面这两个 listener 的作用是更新各大 children count 的数据
@event.listens_for(db.session, 'after_flush')
def flush_listener(session, flush_context):
    dirty_users = getattr(session, 'dirty_users', [])
    for obj in session.dirty:
        if isinstance(obj, UserModel):
            dirty_users.append(obj)
    session.dirty_users = dirty_users


@event.listens_for(db.session, 'after_commit')
def commit_listener(session):
    dirty_users = getattr(session, 'dirty_users', [])

    for user in dirty_users:
        reload_user_meta(user.ukey)
