from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(300), nullable=False)
    category: Mapped[str] = mapped_column(String(80), nullable=False)
    store: Mapped[str] = mapped_column(String(120), nullable=False)
    url: Mapped[str] = mapped_column(String(1000), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    old_price: Mapped[float | None] = mapped_column(Float, nullable=True)
    is_deal: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    checked_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc), nullable=False
    )
