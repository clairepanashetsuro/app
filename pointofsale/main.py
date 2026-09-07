import os

from dotenv import load_dotenv
from fastapi import FastAPI

from app.routers import (
    products,
    customer as customer_router,
    user,
    sales as sales_router,
    sale_item as sale_item_router,
    payment,
    categories,
    suppliers,
    receipts,
)

load_dotenv()

app = FastAPI(
    title=os.getenv("APP_TITLE", "POS API"),
    version=os.getenv("APP_VERSION", "1.0")
)

app.include_router(products.router)
app.include_router(customer_router.router)
app.include_router(user.router)
app.include_router(sales_router.router)
app.include_router(sale_item_router.router)
app.include_router(payment.router)
app.include_router(categories.router)
app.include_router(suppliers.router)
app.include_router(receipts.router)


@app.get("/")
def root():
    return {"message": "Point of Sale API is running successfully"}