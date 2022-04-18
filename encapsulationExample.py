class Employee:
    #constructor
    def __init__(self,name,salary,projects):
        self.name = name
        self.salary = salary
        self.projects = projects
    def show(self):
        print("Name: ",self.name,"salary: ",self.salary)
    def work(self):
        print("Name: ",self.name,"Project: ",self.projects)

emp = Employee("jiwan", 100000, "recordings")
emp.show()
emp.work()