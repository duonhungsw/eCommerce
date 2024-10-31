from sqlalchemy.orm import Session
from model.HomeViewModel import CartItemViewModel
from model.cart import Carts, CartItems
from Repository.HRepository import CartRepository

class CartService:
    def __init__(self, db: Session):
        self.cart_repository = CartRepository(db)

    def getCartByUserId(self, user: dict) -> Carts:
        cart = self.cart_repository.Get_cart_by_id(int(user.get('id')))
        if cart is None:
            return None
        return cart

    def addToCart(self, user: dict, cartItemViewModel: CartItemViewModel) -> CartItems:
        cart = self.getCartByUserId(user)

        if cart is None:
            return {"error": "Cart not found"}

        cartItem = CartItems()
        cartItem.cart_id = cart.id  
        cartItem.product_id = cartItemViewModel.product_id
        cartItem.quantity = cartItemViewModel.quantity
        cartItem.price = cartItemViewModel.price
        cartItem.total_money = cartItemViewModel.total_money
        cartItem.status = cartItemViewModel.status
        
        self.cart_repository.AddToCart(cartItem)

        return cartItem  
