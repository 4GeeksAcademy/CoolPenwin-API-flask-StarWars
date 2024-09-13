"""empty message

Revision ID: 19b46b6fa8e6
Revises: 88df8a843069
Create Date: 2024-09-13 12:58:59.860903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19b46b6fa8e6'
down_revision = '88df8a843069'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('diameter', sa.Float(), nullable=True),
    sa.Column('rotation_period', sa.Integer(), nullable=True),
    sa.Column('orbital_period', sa.Integer(), nullable=True),
    sa.Column('gravity', sa.String(length=250), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('climate', sa.String(length=250), nullable=True),
    sa.Column('terrain', sa.String(length=250), nullable=True),
    sa.Column('surface_water', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('classification', sa.String(length=250), nullable=True),
    sa.Column('designation', sa.String(length=250), nullable=True),
    sa.Column('average_height', sa.String(length=250), nullable=True),
    sa.Column('average_lifespan', sa.String(length=250), nullable=True),
    sa.Column('hair_colors', sa.String(length=250), nullable=True),
    sa.Column('skin_colors', sa.String(length=250), nullable=True),
    sa.Column('eye_colors', sa.String(length=250), nullable=True),
    sa.Column('homeworld', sa.String(length=250), nullable=True),
    sa.Column('language', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('species')
    op.drop_table('planets')
    # ### end Alembic commands ###
