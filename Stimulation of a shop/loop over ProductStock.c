// looping over the products coming from the csv file - customer wants to buy and finding the price what the shop knows 


double find(struct Shop s, char* name)
{
    for (int i=0;i<s.index; i++)
    {
        if (strcmp(name,s.stock[i].product.name) == 0){
            return s.stock[i].product.price;
        }
    }
    return -1;
}

// two products and productstock
int main(void)
{
    struct Product productA= {"Coke Can", 0.0};
    struct Product productB= {"Big Bags", 0.0};

// add in another product 
    struct Product productB= {"Spagetti", 0.0};

    struct Product productA= {productA, 12};
    struct Product productB= {productB, 5};
    struct Product productB= {productC, 2};
// into a array - pull from customer stock ( pointer if you want)

// need to keep track of customer stock

    struct ProductStock array[]= {StockA,StockB, StockC };

    struct Shop shop = createAndStockShop();

// pull out product - access name and pass to the find method - item in shop via its name , 
    for (int i=0;i<3;i++){
        struct Product p = array[i].product;
        double price = find(shop,p.name);

        // find out how much the coke cans will cost the customer 
        //outside loop to calculate the total cost for customer , every itieration of the loop , the sum will be 
        //add to the total cost. print out the total cost outside the loop. 


        double totalCostForcustomer = 0;
        double totalCostOfItem = array[i].quantity*price;
        printf("You want %d of %s, that will cost you %2f\n", array[i].quantity, p.name, totalCostItem);
        printf("The price of %s in the shop is %.2f", p.name, price);
        totalCostForcustomer += totalCostOfItem;
    }

    printf("The total cost for the customer will be  %.2f\n", totalCostForcustomer);
    return 0;

}

//take this example and modify it to take in what is in the csv file , a customer struct
// use logic of the for statement
//if statements for the cost 
// using the customer struct and a pointer

// need to determine can the customer afford it 





