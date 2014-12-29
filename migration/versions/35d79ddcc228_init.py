"""init

Revision ID: 35d79ddcc228
Revises: None
Create Date: 2014-03-11 11:06:14.517684

"""

# revision identifiers, used by Alembic.
revision = '35d79ddcc228'
down_revision = None

from datetime import datetime

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM


def upgrade():
    op.create_table(
        'user',
        sa.Column('ukey', sa.CHAR(8), primary_key=True),
        sa.Column('nickname', sa.Unicode(32)),
        sa.Column('avatar', sa.String(56)),
        sa.Column(
            'gender',
            sa.Enum('male', 'female', name='user_gender_enum')),
        sa.Column('birthday', sa.DateTime()),
        sa.Column('title', sa.Unicode(128)),
        sa.Column('summary', sa.Unicode(512)),
        sa.Column(
            'date_created', sa.DateTime(), default=datetime.now,
            server_default=sa.func.now(),
        ),
    )


def downgrade():
    op.drop_table('user')
    ENUM(name=u'user_gender_enum').drop(
        op.get_bind(), checkfirst=False)
