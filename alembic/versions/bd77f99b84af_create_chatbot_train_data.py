"""create chatbot_train_data

Revision ID: bd77f99b84af
Revises: 
Create Date: 2021-08-30 16:23:56.242272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd77f99b84af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    CREATE TABLE IF NOT EXISTS `chatbot_train_data` (
        `id` INT UNSIGNED COLLATE utf8mb4_unicode_ci NOT NULL AUTO_INCREMENT,
        `intent` varchar(45) COLLATE utf8mb4_unicode_ci NULL,
        `ner` varchar(1024) COLLATE utf8mb4_unicode_ci NULL,
        `query` text COLLATE utf8mb4_unicode_ci NOT NULL,
        `answer` text COLLATE utf8mb4_unicode_ci NOT NULL,
        `answer_image` varchar(2048) COLLATE utf8mb4_unicode_ci NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
    """)


def downgrade():
    op.execute("""
    DROP TABLE `chatbot_train_data`
    """)
    pass
