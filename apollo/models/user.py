#-*- coding: utf-8 -*-

from datetime import datetime

import sqlalchemy as sa

from share.framework.bottle.engines import db
from share.utils.base62 import to_url


__all__ = ['UserModel']


class UserModel(db.Model, db.TableOpt):
    __tablename__ = 'user'

    ukey = sa.Column(sa.CHAR(8), primary_key=True)
    nickname = sa.Column(sa.Unicode(32), nullable=False)
    avatar = sa.Column(sa.String(56))
    gender = sa.Column(
        sa.Enum('male', 'female', name='user_gender_enum'),
        nullable=False
    )
    birthday = sa.Column(sa.DateTime())
    title = sa.Column(sa.Unicode(128))
    summary = sa.Column(sa.Unicode(256))
    date_created = sa.Column(sa.DateTime(), default=datetime.now)

    # setting = sa.relationship(
    #     'setting', uselist=False,
    #     backref=sa.backref('user', lazy='join')
    # )
    def as_dict(self):
        return dict(
            ukey=self.ukey,
            uid=to_url(self.ukey),
            nickname=self.nickname,
            avatar=self.avatar,
            gender=self.gender,
            title=self.title,
            summary=self.summary,
            birthday=self.birthday.isoformat() if self.birthday else '',
            date_created=self.date_created.isoformat(),
        )
