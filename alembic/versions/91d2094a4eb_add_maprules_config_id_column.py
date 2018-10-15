"""add maprules config id column

Revision ID: 91d2094a4eb
Revises: 5002e75c0604
Create Date: 2018-10-15 11:18:50.218921

"""

# revision identifiers, used by Alembic.
revision = '91d2094a4eb'
down_revision = '5002e75c0604'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('project', sa.Column('attribution_config_id', sa.Unicode(), nullable=True))


def downgrade():
    op.drop_column('project','attribution_config_id')

