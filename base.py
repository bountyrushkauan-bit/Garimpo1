from dataclasses import dataclass

@dataclass
class ScrapedProduct:
    name: str
    category: str
    store: str
    url: str
    price: float
    old_price: float | None = None

    @property
    def is_deal(self) -> bool:
        if not self.old_price or self.old_price <= self.price:
            return False
        discount = (self.old_price - self.price) / self.old_price
        return discount >= 0.15
