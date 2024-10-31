from pydantic import BaseModel


class CartItemViewModel(BaseModel):
    id: int
    cart_id: int
    product_id: int
    quantity: int
    price: float
    total_money: float
    status: bool