class New:
    ''' Employee Info '''
    def __init__(self,empname,salary,Desigination):
        self.empname = empname
        self.salary = salary
        self.Desigination = Desigination

#newobj = New('Srinivas Reddy',40000,'Skill Trainer')


print(New('Srinivas',40000,'trainer').empname)
