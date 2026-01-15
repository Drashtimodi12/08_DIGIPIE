# Single Inheritance – Employee & Manager
# Requirements:
# Create class Employee
# method: work() → print “Employee works.”
# Create class Manager(Employee)
# method: manage() → print “Manager manages team.”
# Create object of Manager and access both methods.

class Employee:
    def work(self):
        self.work_done = input("Enter Your Work you do in company: ")
        print("Employee work:", self.work_done)

class Manager(Employee):
    def manage(self):
        print(f"Manager manages employee work: {self.work_done}")

m = Manager()
m.work()
m.manage()
# OP:
# Enter Your Work you do in company: Make.com
# Employee work: Make.com
# Manager manages employee work: Make.com