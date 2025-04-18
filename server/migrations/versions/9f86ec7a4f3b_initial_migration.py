"""Initial migration

Revision ID: 9f86ec7a4f3b
Revises: ad6df61696c5
Create Date: 2025-04-03 22:56:57.004287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f86ec7a4f3b'
down_revision = 'ad6df61696c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('year', sa.Integer(), nullable=True))
    op.add_column('movies', sa.Column('genre', sa.String(), nullable=True))
    op.alter_column('movies', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('movies', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('movies', 'genre')
    op.drop_column('movies', 'year')
    # ### end Alembic commands ###
