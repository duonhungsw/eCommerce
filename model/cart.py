from database import Base
from sqlalchemy import Column, DECIMAL, ForeignKey, Integer,String,Boolean, func
from sqlalchemy.orm import relationship

class Carts(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)



class CartItems(Base):
    __tablename__ = 'cartitems'

    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False) 
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL, nullable=False)
    total_money = Column(DECIMAL, nullable=False)
    status = Column(Boolean, nullable=False)
