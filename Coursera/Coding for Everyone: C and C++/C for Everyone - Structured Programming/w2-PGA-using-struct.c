/*
    Option-02
    Creates a random list of 10 employess
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TOTAL_DEPARTMENT            4

#define HR_STARTER_SALARY           12000
#define SALES_STARTER_SALARY        10000
#define RESEARCH_STARTER_SALARY     15000
#define EXECUTIVE_STARTER_SALARY    20000

#define HR_SALARY_RANGE             5000
#define SALES_SALARY_RANGE          4500
#define RESEARCH_SALARY_RANGE       7500
#define EXECUTIVE_SALARY_RANGE      7000

typedef enum department{
    HR,
    Sales,
    Research,
    Executive
}department;

typedef struct employee{
    department      depart;
    unsigned int    salary;
    unsigned int    social_security_number;
}employee;

//user-defined functions
department set_department(void){return (department)(rand()%TOTAL_DEPARTMENT);}
int set_salary(department depart){
    switch (depart)
    {
    case 0:
        return (rand()%HR_SALARY_RANGE)+HR_STARTER_SALARY;
        break;
    case 1:
        return (rand()%SALES_SALARY_RANGE)+SALES_STARTER_SALARY;
        break;
    case 2:
        return (rand()%RESEARCH_SALARY_RANGE)+RESEARCH_STARTER_SALARY;
        break;
    case 3:
        return (rand()%EXECUTIVE_SALARY_RANGE)+EXECUTIVE_STARTER_SALARY;
        break;
    }
}

int create_social_security_number(void){
    int social;

    social = (rand()%1000)*100;
    social += rand()*100;
    social *= 10000;
    social += rand()%10000;

    return social;
}

employee create_employee(void){
    employee new_employee;

    new_employee.depart                 = set_department();
    new_employee.salary                 = set_salary(new_employee.depart);
    new_employee.social_security_number = (unsigned int)create_social_security_number();

    return new_employee;
}

void print_department(department depart){
    printf("Department: ");
    switch (depart)
    {
    case 0:
        printf("HR\n");
        break;
    case 1:
        printf("Sales\n");
        break;
    case 2:
        printf("Research\n");
        break;
    case 3:
        printf("Executive\n");
        break;
    
    default:
        break;
    }
}

void print_employee_info(employee emp){
    print_department(emp.depart);
    printf("Salary: %u\nSocial Security Number: %u\n", emp.salary, emp.social_security_number);
}


//main function
int main(void){
    employee employee_list[10];
    int i;

    for(i=0; i<10; i++) employee_list[i] = create_employee();
    for(i=0; i<10; i++) print_employee_info(employee_list[i]);

    return 0;
}