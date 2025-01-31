class Employee:
    def __init__(self, name, age, salary, department):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary, department)

class Engineer(Employee):
    def __init__(self, name, age, salary, department, skills):
        super().__init__(name, age, salary, department)
        self.skills = skills

class Company:
    def __init__(self):
        self.departments = {}

    def add_employee(self, employee):
        if employee.department not in self.departments:
            self.departments[employee.department] = []
        self.departments[employee.department].append(employee)

    def find_manager(self, department):
        for emp in self.departments.get(department, []):
            if isinstance(emp, Manager):
                return emp.name
        return None

    def count_employees_in_department(self, department):
        return len(self.departments.get(department, []))

    def count_engineers_with_skill(self, skill):
        count = 0
        for department in self.departments.values():
            for emp in department:
                if isinstance(emp, Engineer) and skill in emp.skills:
                    count += 1
        return count

    def total_employees_per_department(self):
        for department, employees in self.departments.items():
            print(f"Department: {department}, Total Employees: {len(employees)}")

    def total_employees(self):
        return sum(len(emp_list) for emp_list in self.departments.values())

company = Company()

company.add_employee(Manager("Alice", 45, 100000, "IT"))
company.add_employee(Engineer("Bob", 30, 80000, "IT", ["Python", "Java"]))
company.add_employee(Engineer("Charlie", 28, 75000, "IT", ["Java", "C++"]))
company.add_employee(Engineer("David", 35, 82000, "IT", ["Python", "Go"]))

company.add_employee(Manager("Eve", 50, 110000, "HR"))
company.add_employee(Employee("Frank", 40, 60000, "HR"))
company.add_employee(Employee("Grace", 38, 62000, "HR"))

dept = "IT"
print(f"Manager for {dept} department: {company.find_manager(dept)}")
print(f"Total employees in {dept}: {company.count_employees_in_department(dept)}")

skill = "Python"
print(f"Engineers with {skill} skill: {company.count_engineers_with_skill(skill)}")

print("\nTotal employees per department:")
company.total_employees_per_department()

print(f"\nTotal employees in all departments: {company.total_employees()}")
