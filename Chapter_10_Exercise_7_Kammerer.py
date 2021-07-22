class Employee:

    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    def get_info(self):
        print("Name:", self.__name)
        print("ID:", self.__id_number)
        print("Department:", self.__department)
        print("Job Title:", self.__job_title)
        print()


def main():

    susan = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    mark = Employee("Mark Jones", 39119, "IT", "Programmer")
    joy = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

    employees = {"47899": susan, "39119": mark, "81774": joy}
    terminate_loop = False

    while terminate_loop == False:

        print("Please Select an option")
        print("1.) Look up Employee")
        print("2,) Add new Employee")
        print("3.) Change an existing employee data")
        print("4.) Delete an employee's data")
        print("5.) Quit", '\n')

        user_input = int(input("Please Enter Your Decision >>> "))

        if user_input == 1:
            id_input = (input("Please enter the ID of the Employee that you want to look up >>> "))
            if id_input in employees:
                print(employees.get(id_input).get_info())
            else:
                print("Employee not Found")

            end_input = input("Continue? (Y or N) >>> ")

            if end_input == "N" or end_input == "n":
                terminate_loop = True

        elif user_input == 2:
            new_employee_name = input("Please enter the name of the new employee >>> ")
            new_employee_id = input("Please enter the ID of the new Employee >>> ")
            new_employee_department = input("Please enter the Department of the new employee >>> ")
            new_employee_job_title = input("Please enter the job title of the new employee >>> ")

            new_employee = Employee(new_employee_name, new_employee_id,
                                    new_employee_department, new_employee_job_title)

            employees[new_employee_name] = new_employee

            end_input = input("Continue? (Y or N) >>> ")

            if end_input == "N" or end_input == "n":
                terminate_loop = True

        elif user_input == 3:
            employee_change = input("Please enter the ID of the Employee that you want to change >>> ")

            if employee_change in employees:
                new_employee_name = input("Please enter the new name of the employee >>> ")
                new_employee_department = input("Please enter the new Department of the employee >>> ")
                new_employee_job_title = input("Please enter the new job title of the employee >>> ")

                employees[employee_change] = Employee(new_employee_name, employee_change,
                                                      new_employee_department, new_employee_job_title)
            else:
                print("Employee not found")

            end_input = input("Continue? (Y or N) >>> ")

            if end_input == "N" or end_input == "n":
                terminate_loop = True

        elif user_input == 4:
            delete_input = input("Please enter the id of the employee that you want to delete >>> ")

            if delete_input in employees:
                del employees[delete_input]
                print("Done!")
            else:
                print("Name not Found")

            end_input = input("Continue? (Y or N) >>> ")

            if end_input == "N" or end_input == "n":
                terminate_loop = True

        else:
            terminate_loop = True


main()
