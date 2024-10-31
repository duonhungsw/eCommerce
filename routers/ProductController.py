from typing import Annotated
from fastapi import Depends, FastAPI, APIRouter, Path,status, HTTPException
from pydantic import BaseModel, Field
from database import SessionLocal
from sqlalchemy.orm import Session
from models import Products

app = FastAPI()

router = APIRouter(
    prefix='/ProductController',
    tags=['ProductController']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

class ProductRequest(BaseModel):

    name_product: str = Field(min_length=3, max_length=100)
    description: str  = Field(min_length=3, max_length=255)
    picture_url: str  = Field(min_length=3, max_length=255)
    category: str  = Field(min_length=3, max_length=50)
    isDeleted: bool
    price: int

@router.get("/")
async def get_all(db: db_dependency):
    return db.query(Products).all()

@router.get("/getbyid/{id}", status_code=status.HTTP_201_CREATED)
async def getById(db: db_dependency, id: int = Path(gt=0)):
    if id is None:
        raise HTTPException(status_code=404, detail="Id not invalid")
    
    productExist = db.query(Products).filter(Products.id == id).first()

    if productExist is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return productExist

@router.post("/add", status_code=status.HTTP_201_CREATED)
async def add_product(db: db_dependency, productRequest: ProductRequest):
    if productRequest is None:
        raise HTTPException(status_code=404, detail='Do not product in request')
    
    product =  Products()
    product.name_product = productRequest.name_product
    product.description = productRequest.description
    product.picture_url = productRequest.picture_url
    product.category = productRequest.category
    product.isDeleted = productRequest.isDeleted
    product.price = productRequest.price
    # product_model = Products(**product_model.dict(), owner_id=product.get('id'))

    db.add(product)
    db.commit()
    return(product)

@router.patch("/update", status_code= status.HTTP_204_NO_CONTENT)
async def update_product(db: db_dependency, produc_request: ProductRequest, product_id: int = Path(gt=0)):
    if product_id is None:
        raise HTTPException(status_code=404, detail="Not have invalid product")
    
    product_exist = db.query(Products).filter(Products.id == product_id).first()

    if product_exist is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product_exist.name_product = product_exist.name_product
    product_exist.description = product_exist.description
    product_exist.picture_url = product_exist.name_product
    product_exist.category = product_exist.category
    product_exist.isDeleted = product_exist.isDeleted
    product_exist.price = product_exist.price
    db.add(product_exist)
    db.commit()

@router.delete("/delete/{product_id}", status_code=status.HTTP_200_OK)
async def delete_product(db: db_dependency, product_id: int = Path(gt=0)):
    if product_id is None:
        raise HTTPException(status_code=404, detail="Id not invalid")

    product_exist = db.query(Products).filter(Products.id == product_id).first()

    if product_exist is None:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product_exist)
    db.commit()

    