from database import Base
from sqlalchemy import Column, ForeignKey, Integer,String,Boolean


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)  
    username = Column(String(50), unique=True, nullable=False)  
    first_name = Column(String(50), nullable=True)  
    last_name = Column(String(50), nullable=True)  
    hashed_password = Column(String(128), nullable=False)  
    phone_number = Column(String(15), nullable=True)  
    is_active = Column(Boolean, default=True)
    role = Column(String(20), nullable=True)  


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name_product = Column(String(100), nullable=False)  
    description = Column(String(255), nullable=True)  
    picture_url = Column(String(255), nullable=True)  
    category = Column(String(50), nullable=True)  
    isDeleted = Column(Boolean, default=False)
    price = Column(Integer, nullable=True)

