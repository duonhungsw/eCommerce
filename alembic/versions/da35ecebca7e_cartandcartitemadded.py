"""cartAndCartItemAdded

Revision ID: da35ecebca7e
Revises: 0d376486b5d7
Create Date: 2024-10-31 10:51:18.106447

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da35ecebca7e'
down_revision: Union[str, None] = '0d376486b5d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'carts',
        sa.Column('id', sa.Integer, primary_key=True,autoincrement=True, index=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False)  # Khóa ngoại đến users
    )

    # Tạo bảng cartitems
    op.create_table(
        'cartitems',
        sa.Column('id', sa.Integer, primary_key=True,autoincrement=True, index=True),
        sa.Column('cart_id', sa.Integer, sa.ForeignKey('carts.id'), nullable=False),  # Khóa ngoại đến carts
        sa.Column('product_id', sa.Integer,sa.ForeignKey('products.id'), nullable=False),
        sa.Column('quantity', sa.Integer, nullable=False),
        sa.Column('price', sa.DECIMAL, nullable=False),
        sa.Column('total_money', sa.DECIMAL, nullable=False),
        sa.Column('status', sa.Boolean, nullable=False)
    )


def downgrade() -> None:
    # Xóa bảng cartitems trước
    op.drop_table('cartitems')
    # Sau đó xóa bảng carts
    op.drop_table('carts')
