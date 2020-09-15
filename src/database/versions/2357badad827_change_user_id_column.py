"""change user_id column

Revision ID: 2357badad827
Revises: d63d5da1cebb
Create Date: 2020-09-14 23:03:25.657372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2357badad827'
down_revision = 'd63d5da1cebb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('notes_ibfk_1', 'notes', type_='foreignkey')
    op.create_foreign_key(None, 'notes', 'users', ['user_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'notes', type_='foreignkey')
    op.create_foreign_key('notes_ibfk_1', 'notes', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###