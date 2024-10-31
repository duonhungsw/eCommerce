"""priceColumnAdded

Revision ID: 0d376486b5d7
Revises: 
Create Date: 2024-10-31 10:48:29.069580

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d376486b5d7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('products', sa.Column('price', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column('products', 'price')
