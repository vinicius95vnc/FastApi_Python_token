"""adicionando relacionamentos

Revision ID: dbcc5032b94e
Revises: 514a35611a17
Create Date: 2022-04-25 11:55:48.717639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbcc5032b94e'
down_revision = '514a35611a17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('moto', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_cliente', 'cliente', ['cliente'], ['id'])

    with op.batch_alter_table('pedido', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cliente', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('moto', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_cliente', 'cliente', ['cliente'], ['id'])
        batch_op.create_foreign_key('fk_moto', 'moto', ['moto'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedido', schema=None) as batch_op:
        batch_op.drop_constraint('fk_moto', type_='foreignkey')
        batch_op.drop_constraint('fk_cliente', type_='foreignkey')
        batch_op.drop_column('moto')
        batch_op.drop_column('cliente')

    with op.batch_alter_table('moto', schema=None) as batch_op:
        batch_op.drop_constraint('fk_cliente', type_='foreignkey')

    # ### end Alembic commands ###