"""empty message

Revision ID: 36003ebd3bcc
Revises: 14f4eca16e35
Create Date: 2019-03-28 16:02:02.373255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36003ebd3bcc'
down_revision = '14f4eca16e35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('data_sources', sa.Column('namespace', sa.String(length=60), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('data_sources', 'namespace')
    # ### end Alembic commands ###
