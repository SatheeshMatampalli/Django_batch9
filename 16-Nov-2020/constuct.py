class Student:
    ''' this Student class Give more info od student Name and Rollno'''
    def __init__(self,name,rollno,branch):
        self.name = name
        self.rollno = rollno
        self.branch = branch

    def display(self):
        return {'name':self.name,'rollno':self.rollno,'branch':self.branch}


st = Student('Prasanna Raj M',2422.0,'CSE')

print(st.display())
