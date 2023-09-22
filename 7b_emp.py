class Employee:
    def __init__(self):
        self.name = ""
        self.employee_id = ""
        self.department = ""
        self.salary = 0

    def get_employee_details(self):
        self.name = input("Enter Employee name: ")
        self.employee_id = input("Enter Employee ID: ")
        self.department = input("Enter Employee Dept: ")
        self.salary = int(input("Enter Employee Salary: "))

    def show_employee_details(self):
        print("Employee Details")
        print("Name:", self.name)
        print("ID:", self.employee_id)
        print("Dept:", self.department)
        print("Salary:", self.salary)

    def update_salary(self):
        self.salary = int(input("Enter new Salary: "))
        print("Updated Salary:", self.salary)

e1 = Employee()
e1.get_employee_details()
e1.show_employee_details()
e1.update_salary()
