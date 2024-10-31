from fastapi import FastAPI
import models
from database import engine
from routers import  AuthController, CartController, ProductController, UserController
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(AuthController.router)
app.include_router(UserController.router)
app.include_router(ProductController.router)
app.include_router(CartController.router)
