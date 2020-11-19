class Student:
    
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        return{'name':self.name,'rollno':self.rollno}

st=Student('Prasanna Raj M',2422)
print(st.display())
