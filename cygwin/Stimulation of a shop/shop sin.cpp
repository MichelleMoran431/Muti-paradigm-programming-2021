// Week 4 ... building a shop in C

#include <stdio.h>
#include <string.h>
#include <stdlib.h>



struct Product {
	char* name;
	double price;
};

struct ProductStock {
	struct Product product;
	int quantity;
};

struct Shop {
	double cash;
	struct ProductStock stock[20];
		// to keep track of the data in the array
	int index; 
};

// user defined data structure i.e. customer
// needs to be below ProductStock to run correctly
struct Customer {
	char* name;
	// double means it can have a decimal
	double budget;
	// reference to the products bought by the customer
	struct ProductStock shoppingList[10];
	// to keep track of the data in the array
	int index; 
};

// a void method prints out to teh screen, but won't return anything 
// creating a method to print out the product information using structs
// a Product is passed to the method and printed out 
void printProduct(struct Product p)
{
	// printf("--------------\n");
	// sample from main method
	// printf("The %s costs %.2f\n", coke.name, coke.price);
	printf("\nPRODUCT NAME: %s \nPRODUCT PRICE: %.2f\n", p.name, p.price);
	printf("--------------\n");
};


void printCustomer(struct Customer c)
{
	// printf("--------------\n");
	// sample from main method
	// printf("Customer name is %s\n", dominic.name);
	printf("\nCUSTOMER NAME: %s \nCUSTOMER BUDGET: %.2f\n", c.name, c.budget);
	printf("--------------\n");
	for(int i = 0; i < c.index; i++)
	{
	// print what the customer wants to buy from the shopping list
	printProduct(c.shoppingList[i].product);
	
	//print how much of the product they want to buy
	printf("\n%s ORDERS %d OF ABOVE PRODUCT\n", c.name, c.shoppingList[i].quantity);
	
	// calculate the cost of the goods ordered ... quantity x cost
	double cost = c.shoppingList[i].quantity * c.shoppingList[i].product.price;
	printf("The cost to %s will be €%.2f\n", c.name, cost);

	printf("--------------\n");
	
	}
	
};

// stocking the shop and tracking stock
struct Shop createAndStockShop(){
	struct Shop shop = {200};
	
	// reading in from a file 
	// https://stackoverflow.com/questions/3501338/c-read-file-line-by-line
	FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("stock.csv", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, fp)) != -1) {
        // printf("Retrieved line of length %zu:\n", read);
        //printf("%s IS A LINE ", line);
		
		// BREAK OUT THE DATA USING strtok  // 
		// https://www.tutorialspoint.com/c_standard_library/c_function_strtok.htm
		
		// extract the name of the product
		char *n = strtok(line, ",");
		// printf("NAME OF PRODUCT %s\n", name);
		
		// extract the price .. line is Null cause the data is on the same line
		char *p = strtok(NULL, ",");
		// printf("PRICE OF PRODUCT %s\n", price);
				
		// extract the quantity .. line is Null cause the data is on the same line
		char *q = strtok(NULL, ",");
		// printf("QUANTITY OF PRODUCT %s\n", quantity);
		
		// TEST TO EXTRACT CELLS FROM CSV
		//printf("NAME OF PRODUCT IS %s PRICE OF PRODUCT €%s QUANTITY OF PRODUCT IS %s", n, p, q);
		
		// PUTTING THE DATA INTO IT'S CORRECT DATA TYPES using atoi function
		// https://www.tutorialspoint.com/c_standard_library/c_function_atoi.htm
		int quantity = atoi(q);
		
		// atof to convert to a floating point number 
		// https://www.tutorialspoint.com/c_standard_library/c_function_atof.htm
		double price = atof(p);
		
		// to stop variable being overwritten ... malloc funtion to give memory to this variable
		// segmentation error will be the result of excluding malloc
		char *name = malloc(sizeof(char) * 50);
		// string copy = https://www.tutorialspoint.com/c_standard_library/c_function_strcpy.htm
		strcpy(name, n);
		
		struct Product product = { name, price};
		struct ProductStock stockItem = { product, quantity};
		
		// add to the shop
		shop.stock[shop.index++] = stockItem;
		
		printf("NAME OF PRODUCT IS %s PRICE OF PRODUCT €%s QUANTITY OF PRODUCT IS %s", name, price, quantity);
		
	} 
	// get the first item in the shop
	printProduct(shop.stock[0].product);
	return shop;
	
};

void printShop(struct Shop s)
{
	printf("shop has %.2f in cash\n", s.cash);
	for (int i = 0; i < s.index; i++)
	{
		printProduct(s.stock[i].product);
		printf("the shop has %d of the above", s.stock[i].quantity);
	}
}

int main(void)
{
	// call and print the customer 
	//struct Customer dominic = {"Dominic", 100.0};
	//printf("Customer name is %s\n", dominic.name);
	//printCustomer(dominic);
	
	// call and print the product
	//struct Product coke = {"Coke can", 1.10};
	//struct Product bread = {"Bread", 0.70};
	// printf("The %s costs %.2f\n", coke.name, coke.price);
	// call to void printProduct method
	//printProduct(coke);
	
	//call the product stock 
	//struct ProductStock cokeStock = {coke, 20};
	//struct ProductStock breadStock = {bread, 2};
	// printf("The Shop has %d of the product %s\n", cokeStock.quantity, cokeStock.product.name);
	
	// add the product to the customer list ...
	//dominic.shoppingList[dominic.index++] = cokeStock;
	//dominic.shoppingList[dominic.index++] = breadStock;
	//printCustomer(dominic);
	
	//method to create and stock the shop ... no arguments are passed to it
	struct Shop shop = createAndStockShop();
	printShop(shop);
	
	
	return 0;
}

