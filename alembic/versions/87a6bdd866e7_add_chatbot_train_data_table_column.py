"""add chatbot_train_data table column

Revision ID: 87a6bdd866e7
Revises: bd77f99b84af
Create Date: 2021-10-30 22:21:31.051120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87a6bdd866e7'
down_revision = 'bd77f99b84af'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE chatbot_train_data ADD restful_url varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL
        """
    )
    op.execute(
        """
        ALTER TABLE chatbot_train_data ADD res_type varchar(1) COLLATE utf8mb4_unicode_ci DEFAULT NULL
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE chatbot_train_data DROP COLUMN restful_url
        """
    )
    op.execute(
        """
        ALTER TABLE chatbot_train_data DROP COLUMN res_type
        """
    )
