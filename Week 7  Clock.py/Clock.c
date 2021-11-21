//here under procedural, the data is in the struct and the methods exist outside the struct. 
//separate
//OOP the data and methods exist together in a class - uses encapulation and inheritances

// the data from the struct has to be passed into the tick method;

#include<stdio.h>
#include<windows.h>

struct Clock {
    int hours;
    int mins;
    int secs;
};

void tick(struct Clock *c)
{
    c -> secs += 1;

    if (c->secs >59)
    {
        c->mins += 1;
        c->secs =0;
    }

    if (c->mins >59)
    {
        c->hours+= 1;
        c->mins =0;
    }


    if (c->hours >12)
    {
        c->hours= 1;
        c->mins =0;
        c->secs =0;
    }
}

// struct clock here is passed as a clock variable/values. No change to data required 

void printClock (struct Clock c)
{
    printf ("\n Clock");
    printf("\n%02d:%02d:%02d:",c.hours,c.mins,c.secs);
}

// struct Clock is passed as a pointer, as data may need to be changed , called passed by reference. 
// 
void validate (struct Clock *c)
{ 
    if (c-> hours >12 || c->mins>60 || c->secs>60)
    {
        c->hours = 0;
        c->mins = 0;
        c->secs = 0;
    }
}

// stript is the same , a new struct is created ( data container), validation happens outside. 
int main()

{
    struct Clock c ={10, 20, 30};
    validate(&c);
// infinite loop : 1000 miliseconds ( 1sec)
    while (1)
    {
        tick (&c);
        printClock(c);
        Sleep(1000);
    }
    return 0;
}







