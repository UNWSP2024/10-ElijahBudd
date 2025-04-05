# Elijah Budd
# 4/4/2025
# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.

class Employee:
    def __init__(self, name, ID_number, department, job_title):
        self.name = name
        self.ID_number = ID_number
        self.department = department
        self.job_title = job_title

if __name__ == "__main__":
    def employees():
        employee1 = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
        employee2 = Employee('Mark Jones', 39119, 'IT', 'Programmer')
        employee3 = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')

        print('Every employee within the database')
        print('Name   ID Number   Department    Job Title')
        print(employee1.name, employee1.ID_number, employee1.department, employee1.job_title)
        print(employee2.name, employee2.ID_number, employee2.department, employee2.job_title)
        print(employee3.name, employee3.ID_number, employee3.department, employee3.job_title)

    employees()
