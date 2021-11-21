# Muti-paradigm-programming-2021 #

This repository contains the files for the Shop Assignment submitted for the Multi-Paradigm Programming module at GMIT. The actual project was to be submitted through the college Moodle platform as a zip file. This repository serves as a reference for the project.

----------------------------------------------------------------------------

The assignment was to build a Shop program with the functionality as outlined below and to write a report comparing the various programming paradigms used.

### Functionality ###

-The shop CSV should hold the initial cash value for the shop.

-Read in customer orders from a CSV file.

      -That file should include all the products they wish to buy and in what quantity.
      - It should also include their name and their budget.


 - The shop must be able to process the orders of the customer.

  - Update the cash in the shop based on money received.
      -It is important that the state of the shop be consistent.
      -Create customer test files (CSVs) which cannot be completed by the shop e.g customer wants 400 loaves of bread but shop only has 20
      - If these files dont exist penalties will be applied
  - Know whether or not the shop can fill an order
     - Throw an appropriate error


- Operate in a live mode, where the user can enter a product by name, specify a quantity, and pay for it. The user should be able to buy many products in this way.

 - The above described functionality to be completed in both Python and C in a procedural programming style.

 - The functionality of the shop is replicated in an Object Oriented manner using either Python or Java.

 - The live mode, and the input files, should have the exact same behaviour in all implementations with an identical user experience.
 - Have a complete a short report, around 3-5 pages, which compares the solutions achieved using the procedural approach and the object oriented approach





## Repository Content

This README file, a .gitignore and a Licence file

The project instruction in PDF format.

The program code written in both C and Python.

The Python procedural code is in a Python file called shop.py in the python subfolder .
The C procedural code is written in a file called shop.c in the C subfolder.
The object oriented approach is written in Python in a file called shop_oop.py in the python_oop subfolder.
The Project Report in Markdown format.

The Project Report in PDF format.

A stock.csv containing the opening stock and cash of the shop

Several CSV files containing valid customer orders as well as test customer orders which cannot be completed by the shop.


## Running the code ##


### Running the code ###

### Procedural code ###

Navigate to the c folder and run gcc shop.c from the command line to compile the program first into a file called a.out. Once compiled the program can be run using the command ./a.out.
Navigate to the python folder and use the command python shop.py to run the program from the command line.

### Object Oriented Style 
###
Navigate to the python_oop folder and use the command python shop_oop.py to run the program from the command line.


### The user interface ###

The interface for the user is the same for all 3 versions of the program. The user is present with a display menu that has 3 options available.

Option 1 is to print the current shop state. This will show the cash and stock amounts in the shop whenever it is called. Initially the shop cash and stock items are read from a csv file called stock.csv. Once read in the file is no longer used.

Option 2 gives the user the option to act as a customer that has an order in a file. The user is asked to enter the name of the file. The user should just enter the name of the file without the .csv extension. For example a file named customer.csv is just entered as customer and likewise with all the other customer files.

Option 3 gives the user the option to enter a live mode, where the user can enter a product by name, specify a quantity, and pay for it. The user can buy many products in this way.


### Test files ###

There are several test files in the main folder.

 - customer.csv, customer1.csv and customer2.csv are customer file containing orders that the shop can fill from the stock at the start of the program execution. The shop stock and cash is updated after every successful order has been processed whether this is a live or batch order. Therefore it is possible that one of these orders cannot be completly filled if the shop stock has already been sold.
 
There are also some test files as required that the shop cannot completely fulfill.

 - fred.csv contains an item that the shop does not stock at all.
 - joe.csv contains several products that the shop does not stock at all.
 - mike.csv contains two products, including one item that the shop does not stock.
 - bad.csv and broke.csv are customer files where the customer does not have enough cash to pay for their shopping order.
 - poor.csv is a customer file where the customer does not have enough cash to purchase all the items on their shopping order.
 - coke.csv is a customer file where the customer is looking for a higher quantity of a product than the shop has in stock.


