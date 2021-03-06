"""changeed DBActivity.blob to DBActivity.pickle

Revision ID: f78b2382cb82
Revises: 18d461d233f1
Create Date: 2021-08-09 23:25:23.450502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f78b2382cb82'
down_revision = '18d461d233f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('db_activity', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pickle', sa.LargeBinary(), nullable=True))
        batch_op.drop_column('blob')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('db_activity', schema=None) as batch_op:
        batch_op.add_column(sa.Column('blob', sa.LargeBinary(), nullable=True))
        batch_op.drop_column('pickle')

    # ### end Alembic commands ###
