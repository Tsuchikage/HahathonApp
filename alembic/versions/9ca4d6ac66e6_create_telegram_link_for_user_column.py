"""Create telegram link for user column

Revision ID: 9ca4d6ac66e6
Revises: 
Create Date: 2023-11-19 14:47:52.367742

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ca4d6ac66e6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('usercards', sa.Column('telegram_link', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('usercards', 'telegram_link')
