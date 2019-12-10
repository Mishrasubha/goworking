"""empty message

Revision ID: 97b6faa5a92c
Revises: dc7d560eee94
Create Date: 2019-12-10 13:55:44.607858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97b6faa5a92c'
down_revision = 'dc7d560eee94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cadeira_v1', sa.Column('desc', sa.Text(), nullable=True))
    op.add_column('mesa_v1', sa.Column('desc', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mesa_v1', 'desc')
    op.drop_column('cadeira_v1', 'desc')
    # ### end Alembic commands ###