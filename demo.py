from .base import ScrapedProduct

def demo_products() -> list[ScrapedProduct]:
    return [
        ScrapedProduct(
            name="SSD NVMe 1TB — Demonstração",
            category="SSD",
            store="Loja Demo",
            url="https://example.com",
            price=699.90,
            old_price=899.90,
        ),
        ScrapedProduct(
            name='Monitor QHD 27" 180Hz — Demonstração',
            category="Monitor",
            store="Loja Demo",
            url="https://example.com",
            price=849.90,
            old_price=999.90,
        ),
        ScrapedProduct(
            name="Ryzen 5 — Demonstração",
            category="CPU",
            store="Loja Demo",
            url="https://example.com",
            price=999.90,
            old_price=1099.90,
        ),
    ]
