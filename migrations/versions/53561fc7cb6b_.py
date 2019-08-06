"""empty message

Revision ID: 53561fc7cb6b
Revises: 
Create Date: 2019-08-06 01:42:27.535657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53561fc7cb6b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###