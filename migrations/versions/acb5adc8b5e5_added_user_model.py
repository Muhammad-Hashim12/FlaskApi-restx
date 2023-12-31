"""added user model 

Revision ID: acb5adc8b5e5
Revises: 
Create Date: 2023-07-16 17:50:02.789670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acb5adc8b5e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('cource', schema=None) as batch_op:
        batch_op.add_column(sa.Column('instructor_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'user', ['instructor_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cource', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('instructor_id')

    op.drop_table('user')
    # ### end Alembic commands ###
