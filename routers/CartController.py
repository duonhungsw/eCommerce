from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal
from routers.AuthController import get_current_user
from services.CartService import CartService
from typing import Annotated

router = APIRouter(prefix='/CartController', tags=['CartController'])

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class CartItemViewModel(BaseModel):
    product_id: int
    quantity: int
    price: float
    total_money: float
    status: bool

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/get_user", status_code=status.HTTP_200_OK)
async def getUser(db: Session = Depends(get_db), user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    
    cart_service = CartService(db)  # Khởi tạo dịch vụ với db
    cart = cart_service.getCartByUserId(user)
    if cart is None:
        raise HTTPException(status_code=404, detail='Not found cart of user')  
    
    return cart

@router.post("/add_to_cart", status_code=status.HTTP_201_CREATED)
async def addToCart(cartItemViewModel: CartItemViewModel, user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')

    cart_service = CartService(SessionLocal())  # Khởi tạo dịch vụ với db
    return cart_service.addToCart(user, cartItemViewModel)



