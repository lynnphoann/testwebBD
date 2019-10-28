import eel
from service import *

eel.init('web')

s = Service()


@eel.expose
def insertDish(name, price):
    return s.insertDish(name, price)

@eel.expose 
def getAllDish():
    result = s.getAllDish()
    lisy = []
    for dish in result:
        lisy.append([dish.id, dish.name, dish.price])
    return lisy

@eel.expose
def getDishByid(id):
    dish = s.getDishByid(id)
    return [dish.id,dish.name,dish.price]

@eel.expose
def updateDish(id, name, price):
    return s.updateDish(id, name, price)


@eel.expose
def deleteDish(id):
    return s.deleteDish(id)

@eel.expose 
def createTable(name):
    return s.createTable(name)

@eel.expose 
def getAllTable():
    result = s.getAllTable()
    lisy = []
    for table in result:
        lisy.append([table.id, table.name, table.status])
    return lisy

@eel.expose 
def getTableById(id):
    result =  s.getTableById(id)
    return [result.id,result.name]

@eel.expose
def updateTable(id,name):
    return s.updateTable(id,name)

@eel.expose 
def updateTableStatus(id):
    return s.updateTableStatus(id)

@eel.expose 
def deleteTable(id):
    return s.deleteTable(id)

@eel.expose 
def insertOrder(table_id,dish_id,dish_count):
    return s.insertOrder(table_id, dish_id, dish_count)

@eel.expose 
def getOrderById(id):
    return s.getOrderById(id)

@eel.expose 
def updateOrder(id,table_id,dish_id,dish_count):
    return s.updateOrder(id, table_id, dish_id, dish_count)

@eel.expose 
def getAllOderBytable(table_id):
    return s.getAllOderBytable(table_id)

@eel.expose 
def updateOrderStatus(id):
    return s.updateOrderStatus(id)


eel.start('index.html')
