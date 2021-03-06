"""new fields in user model

Revision ID: 0477b04c78be
Revises: 4db125c5b1f7
Create Date: 2019-01-10 11:00:51.319761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0477b04c78be'
down_revision = '4db125c5b1f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
