from pathlib import Path

from fastapi import Depends, FastAPI, Query
from fastapi.responses import HTMLResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from .config import settings
from .database import get_db, init_db
from .models import Product
from .schemas import ProductCreate, ProductOut

app = FastAPI(title=settings.app_name, version="1.0.0")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok", "app": settings.app_name}

@app.get("/api/products", response_model=list[ProductOut])
def get_products(
    category: str | None = Query(default=None),
    deals_only: bool = False,
    db: Session = Depends(get_db),
):
    statement = select(Product).order_by(Product.price.asc())
    if category:
        statement = statement.where(Product.category == category)
    if deals_only:
        statement = statement.where(Product.is_deal.is_(True))
    return list(db.scalars(statement).all())

@app.post("/api/products", response_model=ProductOut, status_code=201)
def create_product(product_data: ProductCreate, db: Session = Depends(get_db)):
    product = Product(**product_data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

@app.get("/", response_class=HTMLResponse)
def home():
    html_path = Path(__file__).resolve().parent.parent / "static" / "index.html"
    return HTMLResponse(html_path.read_text(encoding="utf-8"))
