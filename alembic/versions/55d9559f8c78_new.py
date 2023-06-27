"""New

Revision ID: 55d9559f8c78
Revises: 8f28ce7a1caa
Create Date: 2023-06-27 23:22:18.068225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55d9559f8c78'
down_revision = '8f28ce7a1caa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('profiles', sa.Column('updated_at', sa.DateTime(), nullable=False))
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('users', sa.Column('updated_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    op.drop_column('profiles', 'updated_at')
    op.drop_column('profiles', 'created_at')
    # ### end Alembic commands ###