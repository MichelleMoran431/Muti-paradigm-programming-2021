from dataclasses import dataclass, field
from typing import List
import csv


# dataclass = data container ( like a struc) 
#python is dynamically - the variables can change over time , that is it can be a float or string. where as c , it is always the one thing 
# no memory allocation




# Product is a data container here only. 
# This is equivalent to the product Struct in C
#dataclass 
class Product:
    name:str
    price:float = 0.0

#This is equivalent to the ProductStock Struct in C
#dataclass
class ProductStock:
    product: Product
    quantity:int

# A data container for a Shop
class Shop:
    cash: float = 0.0
    stock: List[ProductStock]= field(default_factory=list)

#dataclass
class Customer:
    name:str = ""
    budget:float = 0.0
    shopping_List:List[ProductStock]= field(default_factory=list)


## csv reader : allows reading of the individual rows


def create_and_stock_shop():
    # Shop is a dataclass with cash (float) and stock (list of productStock)
    s= Shop()
     # read in csv file and get shop cash from first row
    with open('stock.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        #print(first_row)
        s.cash = float(first_row[0])
        # iterate through the rows of the csv file creating Product, ProductStock and shop stock using the 
        # data classes defined earlier.
        for row in csv_reader:
            p= Product(row[0],float(row[1]))
            ps = ProductStock (p,float(row[2]))
            s.stock.append(ps)
            #print(ps)
      # return the shop dataclass      
    return s


#   read in customer csv file, customer enters file name only
def read_customer(file_path):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        # customer name is col 0 of row 0, customer budget is col 1 of row 0
        c = Customer(first_row[0],float(first_row[1]))
        # iterate through the rest of the rows of the file (after the first row)
        #print(c)
        for row in csv_reader:
             # product name is the first col
            name = row[0]
            # product quantity is the second column
            quantity = float(row[1])
            # Product is a dataclass with name (str) and price (float)
            p = Product (name)
            # ProductStock is a dataclass with Product (a dataclass with product name and price)
            ps = ProductStock (p,quantity)
             # ps will have Product name, Product price and a quantity
            c.shopping_list.append(ps)
        return c 




#Methods for printing 
# Takes in a product and prints out the price
def print_product (p):
    print(f'\nPRODUCT NAME: { p.name} \nPRODUCT Price:{ p.price}')

def print_customer (c):
    print(f'\nCUSTOMER NAME: { c.name} \nCUSTOMER BUDGET:{ c.BUDGET}')

    for item in c.shopping_list:
        print_product(item.product)

        print(f'{c.name} ORDERS {item.quantity} OF ABOVE PRODUCT')
        cost = item.quantity* item.product.price
        print(f'The cost to  {c.name} will be {cost}')


# This function prints the cash in the shop  and each 
def print_shop(s) :
    print(f'Shop has {s.cash} in cash')
    for item in s.stock:
        # call print_product to print out each product name, price and quantity
        print_product (item.product)
        print(f'The Shop has {item.quantity} of the above')
        print('-------------')

s = create_and_stock_shop()
print_shop(s)
c = read_customer("Customer 1.csv")
print_customer(c)