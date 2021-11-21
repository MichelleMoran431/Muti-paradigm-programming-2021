
// reading in from the csv file 

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<errno.h>

struct Customer{
    char*name;
    double budget;

};

struct Customer custOrder()
{

    FILE*fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;

    fp=fopen("Customer1.csv","r");
    if (fp==NULL)
        exit (EXIT_FAILURE);



// reading from the first line of the csv file - the name and how much 
// getline pulls info from the 1st and strtok tears it apart , the name goes into a and the budget goes into b 
// create a memory to store it . 
    read = getline(&line,&len,fp);
    char*a = strtok(line,",");
    char*b = strtok(NULL, ",");
    char *custName= malloc (sizeof(char) *50);
    double custBudget = atof(b);
    strcpy (custName,a);
    struct Customer customer = {custName, custBudget};

    while((read = getline(&line, &len, fp)) != -1){

        //TODO process remaining lines
    }
    return customer;
    }

    int main(void)
    {
        struct Customer customer = custOrder();
        printf(" Customer name is : %s and they have: %.2f for their budget\n", customer.name, customer.budget);
        return 0;
    }