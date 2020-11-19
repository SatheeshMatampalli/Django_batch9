'''
class Hello: # Create a class
    a = 100
    b = 200
    c = "APSSDC"

    def hai(): # Userdefined Function
        print("Django Workshop")
        print("APSSDC_Tadepalli")
        
Hello.hai() # Calling Function

print(Hello.a,Hello.b)
print(Hello.c)

class Math():
    def addition(a,b):
        return a+b
    def substraction(a,b):
        return a-b
    def multification(a,b):
        return a*b
# Craete a Object

mt = Math   # objname = ClassName

print("ADD is:",mt.addition(10,20))
print("SUB is:",mt.substraction(100,20))
print("MUL is:",mt.multification(5,5))


print(Math.addition(100,200))
print(Math.substraction(100,200))


class Apssdc:
    def t1():
        t = ['Prasanna Raj','Satheesh','Srinivas']
        return t
    def d1():
        d = ['Multiskill','Software Trainee','TrainercumDeveloper']
        return d
    def empids():
        empid = (1429,26,2422)
        return empid

# obj = Apssdc

print(Apssdc.t1())
print(Apssdc.d1())
print(Apssdc.empids())

'''

class mathopertions:
    a = 100
    b = 200
    c = 300
    def add():
        return MO.a + MO.b + MO.c
    def multify():
        return MO.a * MO.b * MO.c
MO = mathopertions

print(MO.add())
print(MO.multify())




    


    






        
