"""shedule

Revision ID: e36e4900cef2
Revises: 8d26623c329d
Create Date: 2021-09-05 14:14:21.532614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e36e4900cef2'
down_revision = '8d26623c329d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'admin_user', ['id'])
    op.add_column('bot_user', sa.Column('shedule', sa.Time(), nullable=True))
    op.drop_constraint('bot_user_chat_id_key', 'bot_user', type_='unique')
    op.create_unique_constraint(None, 'bot_user', ['id'])
    op.drop_column('bot_user', 'chat_id')
    op.create_unique_constraint(None, 'tag', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tag', type_='unique')
    op.add_column('bot_user', sa.Column('chat_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'bot_user', type_='unique')
    op.create_unique_constraint('bot_user_chat_id_key', 'bot_user', ['chat_id'])
    op.drop_column('bot_user', 'shedule')
    op.drop_constraint(None, 'admin_user', type_='unique')
    # ### end Alembic commands ###
