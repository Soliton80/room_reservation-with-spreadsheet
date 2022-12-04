"""Add reservation model

Revision ID: 3c08704f7fad
Revises: b90b2273b106
Create Date: 2022-11-20 13:21:53.936722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c08704f7fad'
down_revision = 'b90b2273b106'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_reserve', sa.DateTime(), nullable=True),
    sa.Column('to_reserve', sa.DateTime(), nullable=True),
    sa.Column('meetingroom_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['meetingroom_id'], ['meetingroom.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    # ### end Alembic commands ###
