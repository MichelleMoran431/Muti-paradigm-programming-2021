#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Module {
    char name [50];
};

struct Student {
    struct Module modules [10];
};

struct Manager {
    char name [50];
    int age ;
    float salary ;
    int Employees;

};

void printModule (struct Module module){
    printf("The module name is %s\n" , module.name);
};

void printManager(struct Manager manager,manager.name){
    printf("The manager name is %s\n" , manager.name);

int main(void)
{
    struct Module module = {"Multiparadigm Programming" };
    printModule( module);

    struct Student student ={};
    student.modules[0];
    
    struct Module module2 = {"Introduction to Programming" };
    student.modules[1] = module2;

    struct Manager manager = {"Michelle Moran"};
    printManager (manager.name);

    printModule(student.modules[0]);
    printModule(student.modules[1]);
    printManager(manager.name);
        return 0;
}