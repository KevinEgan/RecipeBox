"""migrationTest

Revision ID: 9a02f6b0dd7a
Revises: 
Create Date: 2025-03-17 22:07:25.614940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a02f6b0dd7a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('migration_test', sa.String(length=20), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.drop_column('migration_test')

    # ### end Alembic commands ###
