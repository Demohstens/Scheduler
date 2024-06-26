"""Added Untis Login validator

Revision ID: 3771c627fde6
Revises: b5df9bd2a93f
Create Date: 2024-04-30 23:46:28.072536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3771c627fde6'
down_revision = 'b5df9bd2a93f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('untis_login_valid', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('untis_login_valid')

    # ### end Alembic commands ###
