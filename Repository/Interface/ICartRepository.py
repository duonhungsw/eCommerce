from abc import ABC, abstractmethod
from typing import List
from model.cart import CartItems , Carts

class ICartRepository(ABC):

    @abstractmethod
    def Get_cart_by_id(self, cart_id: int) -> Carts:
        pass

    @abstractmethod
    def AddToCart(self, CartItem: CartItems) -> CartItems:
        pass

    @abstractmethod
    def list_cartItems(self,user_id: int) -> List[CartItems]:
        pass