"""empty message

Revision ID: 73351cf7b04a
Revises: ed58acc96876
Create Date: 2021-01-06 17:26:27.621701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73351cf7b04a'
down_revision = 'ed58acc96876'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('Artist', sa.Column('show_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Artist', 'Shows', ['show_id'], ['id'])
    op.add_column('Venue', sa.Column('show_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Venue', 'Shows', ['show_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Venue', type_='foreignkey')
    op.drop_column('Venue', 'show_id')
    op.drop_constraint(None, 'Artist', type_='foreignkey')
    op.drop_column('Artist', 'show_id')
    op.drop_table('Shows')
    # ### end Alembic commands ###
