from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from db import *
class Service:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def insertDish(self,name,price):
        new_dish = Dish(name=name,price=price)
        self.session.add(new_dish)
        return self.session.commit()

    def getAllDish(self):
        return self.session.query(Dish).all()

    def getDishByid(self,id):
        return self.session.query(Dish).get(id)

    def updateDish(self,id,name,price):
        dish = self.getDishByid(id)
        dish.name = name
        dish.price = price 
        return self.session.commit()

    def deleteDish(self,id):
         dish = self.getDishByid(id)
         self.session.delete(dish)
         return self.session.commit()

    def createTable(self,name):
        new_table = Table(name=name)
        self.session.add(new_table)
        return self.session.commit()

    def getAllTable(self):
        return self.session.query(Table).all()

    def getTableById(self, id):
        return self.session.query(Table).get(id)

    def updateTable(self,id,name):
        table = self.getTableById(id)
        table.name = name 
        self.session.commit()

    def updateTableStatus(self,id):
        table = self.getTableById(id)
        table.status = 0 
        self.session.commit()

    def deleteTable(self,id):
        table = self.getTableById(id)
        self.session.delete(table)
        self.session.commit()

    def insertOrder(self,table_id,dish_id,dish_count):
        new_oreder = Order(table_id=table_id,dish_id=dish_id,dish_count=dish_count)
        self.session.add(new_oreder)
        self.session.commit()

    def getOrderById(self,id):
        order = self.session.query(Order).get(id)
        self.session.commit()
        return order

    def updateOrder(self,id,table_id,dish_id,dish_count):
        order = self.getOrderById(id)
        order.table_id = table_id
        order.dish_id = dish_id
        order.dish_count = dish_count
        self.session.commit()

    def getAllOderBytable(self,table_id):
        orders = self.session.query(Order).filter(text("table_id = :value")).params(value = table_id)
        self.session.commit()
        return orders

    def updateOrderStatus(self,id):
        order = self.getOrderById(id)
        order.statue = 0
        self.session.commit()

