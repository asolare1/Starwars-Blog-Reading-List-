"""empty message

Revision ID: 0750869e5abe
Revises: 
Create Date: 2023-03-28 14:57:03.587626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0750869e5abe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('mass', sa.String(length=256), nullable=True),
    sa.Column('hair_color', sa.String(length=256), nullable=True),
    sa.Column('skin_color', sa.String(length=256), nullable=True),
    sa.Column('eye_color', sa.String(length=256), nullable=True),
    sa.Column('birth_year', sa.String(length=256), nullable=True),
    sa.Column('gender', sa.String(length=256), nullable=True),
    sa.Column('homeworld', sa.String(length=256), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('planets',
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('rotation_period', sa.Integer(), nullable=True),
    sa.Column('orbital_period', sa.Integer(), nullable=True),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('climate', sa.String(length=256), nullable=True),
    sa.Column('gravity', sa.Integer(), nullable=True),
    sa.Column('terrain', sa.String(length=256), nullable=True),
    sa.Column('surface_water', sa.Integer(), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planets_name', sa.String(length=256), nullable=True),
    sa.Column('people_name', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('user')
    op.drop_table('planets')
    op.drop_table('people')
    # ### end Alembic commands ###
