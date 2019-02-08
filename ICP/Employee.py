class Employee:
    'Common base class for all employees'
    empCount = 0
    salaries = []

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.empCount += 1
        Employee.salaries.append(self.salary)

    def avgSalary(self,salaries):
        totalSal = 0
        for sal in salaries:
            totalSal = totalSal + sal
        return totalSal/self.empCount

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)


emp = Employee('chandu','hindu',100000,'IT')
emp.displayEmployee()
emp1 = Employee('bantu','hindu',200000,'IT')
print("EMployee Count:: ",emp.empCount)
print("Employee avg salary::",emp.avgSalary(salaries=emp1.salaries))
