from sqlalchemy import create_engine, Column, Integer, String, Float
# ... (igual al anterior pero con modelo Product)
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
# ...
