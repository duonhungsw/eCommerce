from typing import Annotated, List
from fastapi import Depends
from sqlalchemy.orm import Session
from Repository.Interface import ICartRepository
from model.cart import CartItems, Carts
from routers.AuthController import get_db

db_dependency = Annotated[Session, Depends(get_db)]

class CartRepository(ICartRepository.ICartRepository):
    def __init__(self, db: Session):
        self.db = db

    def Get_cart_by_id(self, cart_id: int) -> Carts:
        return self.db.query(Carts).filter(Carts.id == cart_id).first()
    
    def AddToCart(self, cartItem: CartItems) -> CartItems:
        self.db.add(cartItem)
        self.db.commit()
        self.db.refresh(cartItem)
        return cartItem

    def list_cartItems(self, cart_id: int) -> List[CartItems]:
        return self.db.query(CartItems).filter(CartItems.cart_id == cart_id).all()