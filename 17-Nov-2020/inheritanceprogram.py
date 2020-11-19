'''class ClassA: # Parent Class Data
    def method1():
        return 'I am from ClassA, method1'
class ClassB(ClassA): # Child Class Data
    def method2():
        return 'I am from ClassB, method2'

obj = ClassB

obj.method2
#obj.method1
'''

# Multiple Inheritances

class ParentA:
    def method1():
        return 'ParentA'
class ParentB:
    def method2():
        return 'ParentB'
class Child(ParentA,ParentB):
    def method3():
        return 'Iam Child Class'

abc = Child # Create a Object

print(abc.method3())

# Acess ParentA and ParentB Class Data 
print(abc.method1(),abc.method2())








