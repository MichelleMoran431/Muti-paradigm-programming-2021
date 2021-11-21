## OBJECT ORIENTED PROCEDURE :
# 4 CLASSES 
#() calling a method 


import csv

class Product:

    def __init__(self, name, price=0):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f'NAME: {self.name} PRICE: {self.price}'

class ProductStock:
    
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    def name(self):
        return self.product.name;
    
    def unit_price(self):
        return self.product.price;
        
    def cost(self):
        return self.unit_price() * self.quantity
        
    def __repr__(self):
        return f"{self.product} QUANTITY: {self.quantity}"


# core of program : __init__ constructor.  pulls in information from csv file . new customers can be put into an instance of customer class
# examples of customer - one that has enough money, one that has partial amount , and customer not enough
# self keyword and variable name stores information from csv file


class Customer:

    def __init__(self, path):
        self.shopping_list = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.name = first_row[0]
            self.budget = float(first_row[1])
            for row in csv_reader:
                name = row[0]
                quantity = float(row[1])
                p = Product(name)
                ps = ProductStock(p, quantity)
                self.shopping_list.append(ps) 
                
    # passing in the stock array comes from shop ( s.shop) , comes in as price list , for every item in shop, check against what i want to buy, if its match , save the price of it and calculate the cost. 
    
    def calculate_costs(self, price_list):
        for shop_item in price_list:
            for list_item in self.shopping_list:
                if (list_item.name() == shop_item.name()):
                    list_item.product.price = shop_item.unit_price()
    
    def order_cost(self):
        cost = 0
        
        for list_item in self.shopping_list:
            cost += list_item.cost()
        
        return cost
    
    def __repr__(self):
        
        str = f"{self.name} wants to buy"
        for item in self.shopping_list:
            cost = item.cost() # calculate the cost of item , product stock class called to calculate cost
            str += f"\n{item}"
            if (cost == 0):  # no free items in shop, missing stock info price
                str += f" {self.name} doesn't know how much that costs :("
            else:
                str += f" COST: {cost}" # prints cost
                
        str += f"\nThe cost would be: {self.order_cost()}, he would have {self.budget - self.order_cost()} left"
        return str 


# CONSTRUCTOR -  PATH TO CSV INFORMATION TO SET UP THE SHOP. 
# FUNCTIONALITY INSIDE SHOP CLASS
#        
class Shop:
    
    def __init__(self, path):
        self.stock = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.cash = float(first_row[0])
            for row in csv_reader:
                p = Product(row[0], float(row[1]))
                ps = ProductStock(p, float(row[2]))
                self.stock.append(ps)


#  RETURNS A TEXT BASED REPRESENTATION OF THE SHOP IN ITS STATE , CREATES A STRING , APPENDS WITH SHOP STOCK
    def __repr__(self):
        str = ""
        str += f'Shop has {self.cash} in cash\n'
        for item in self.stock:
            str += f"{item}\n"
        return str

s = Shop("stock.csv")
print(s)

c = Customer("Customer 1.csv")
c.calculate_costs(s.stock)
print(c)

# a method where the customer can contact the shop stock and calculate the cost