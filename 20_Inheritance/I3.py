# Multiple Inheritance – Teacher & Researcher
# Requirements:
# Class Teacher – method teach()
# Class Researcher – method research()
# Class Professor(Teacher, Researcher)
# method: guide()
# Create object of Professor and call all methods.

class Teacher:
    def teach(self):
        print("I work as a teacher to tech student.")

class Researcher:
    def research(self):
        print("I am researcher to research student growth.")

class Professor(Teacher, Researcher):
    def guide(self):
        print("I am professor to see teacher and researcher work properly...")


p = Professor()
p.teach()
p.research()
p.guide()
# OP: 
# I work as a teacher to tech student.
# I am researcher to research student growth.
# I am professor to see teacher and researcher work properly...
