from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///mydb.db")

Base = declarative_base()

class Table(Base):
    __tablename__ = "tables"
    id = Column(Integer,primary_key=True) 
    name = Column(String)
    status = Column(Integer,default=0)

class Dish(Base):
    __tablename__ = "dishes"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    table_id = Column(Integer,ForeignKey("tables.id"))
    dish_id = Column(Integer,ForeignKey("dishes.id"))
    dish_count = Column(Integer,default=1)
    statue = Column(Integer,default=1)
    table = relationship("Table", back_populates="orders")
    dish = relationship("Dish",back_populates="orders")


Table.orders = relationship("Order", back_populates="table")
Dish.orders = relationship("Order", back_populates="dish")


Base.metadata.create_all(engine)