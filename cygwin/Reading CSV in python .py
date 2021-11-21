

from dataclasses import dataclass, field
from typing import List
import csv

class Product:
    name: str
    price:float = 0.0

class ProductStock:
    product: Product
    quantity:int

class Shop:

    cash:float =0.0
    stock:List[ProductStock]= field(default_factor=list)

class Customer:
    name:str = ""
    budget:float = 0
    shopping_list: List [ProductStock]= field(default_factor=list)


def create_and_stock_shop():

    s = Shop()
    with open('../stock.csv')as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        first_row=next(csv_reader)
        print(first_row)
        s.cash= float(first_row[0])
        for row in csv_reader:
            p = Product(row[0],float,(row[1])
            ps= ProductStock(p, float(p,row[2]))
            s.stock.append(ps)
            #print(ps)
        return s

def read_customer(file_path):
    with open('../customer.csv')as a csv_file:
        csv_reader = csv_reader(csv_file,delimiter=',')
        first_row= next ( csv_reader)
        c = Customer( first_row[0], float( fist_row[1])
        print (c)
        for row in csv_reader:
            name = row[0]
            quantity= float(row[1])
            p = product(name)
            ps = ProductStock( p, quantity)
            c.shopping_list.appen(ps)
        return c 
           






def print_product(p):
    print(f'\nPRODUCT NAME: {p.name} \nPRODUCT PRICE: {p.price} ')

def print_customer(c):
    print(f'\nCUSTOMER NAME: {c.name} \nCUSTOMER BUDGET: {c.budget} ')

    for item in c.shopping_list:
        print_product(item.product)

        print(f'{c.name} ORDERS {item.quanitity} OF ABOVE PRODUCT'
        cost = item.quanitity*item.product.price
        print(f'The cost to {c.name} will be {cost}')

def print_shop(s)
    print (f'Shop has {s.cash} in cash')
    for item in s.stock:
        print_product(item.product)
        print (f'The Shop has {item.quantity} of the above')

s = create_and_stock_shop()
print_Shop(s)

c = read_customer("../customer.csv")
print_customer(c)

