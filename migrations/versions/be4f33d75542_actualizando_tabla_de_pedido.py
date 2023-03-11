"""Actualizando tabla de pedido

Revision ID: be4f33d75542
Revises: c9c0f01be4d7
Create Date: 2023-03-03 12:54:58.031718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be4f33d75542'
down_revision = 'c9c0f01be4d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedidos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('estado', sa.String(length=120), nullable=True))
        batch_op.drop_column('status')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedidos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.BOOLEAN(), autoincrement=False, nullable=True))
        batch_op.drop_column('estado')

    # ### end Alembic commands ###