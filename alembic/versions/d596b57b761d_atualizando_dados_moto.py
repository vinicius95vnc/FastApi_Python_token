"""atualizando dados moto

Revision ID: d596b57b761d
Revises: 156869f25f58
Create Date: 2022-04-27 13:54:19.715645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd596b57b761d'
down_revision = '156869f25f58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('moto', schema=None) as batch_op:
        batch_op.add_column(sa.Column('observacao', sa.String(), nullable=True))
        batch_op.drop_column('obs')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('moto', schema=None) as batch_op:
        batch_op.add_column(sa.Column('obs', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('observacao')

    # ### end Alembic commands ###