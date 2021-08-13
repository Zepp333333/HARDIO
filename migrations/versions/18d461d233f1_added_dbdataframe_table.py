"""added DBDataFrame table

Revision ID: 18d461d233f1
Revises: 0713a93f9308
Create Date: 2021-08-06 16:12:44.889682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18d461d233f1'
down_revision = '0713a93f9308'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('db_data_frame',
    sa.Column('activity_id', sa.Integer(), nullable=False),
    sa.Column('df_json', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['activity_id'], ['db_activity.activity_id'], ),
    sa.PrimaryKeyConstraint('activity_id')
    )
    with op.batch_alter_table('db_activity', schema=None) as batch_op:
        batch_op.add_column(sa.Column('df_json', sa.JSON(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('db_activity', schema=None) as batch_op:
        batch_op.drop_column('df_json')

    op.drop_table('db_data_frame')
    # ### end Alembic commands ###