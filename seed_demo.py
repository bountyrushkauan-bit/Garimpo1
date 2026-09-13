from app.database import SessionLocal, init_db
from app.services.import_demo import import_demo

def main():
    init_db()
    with SessionLocal() as db:
        total = import_demo(db)
    print(f"Importados: {total} produtos.")

if __name__ == "__main__":
    main()
