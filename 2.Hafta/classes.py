class Maths:
    def topla(self,sayi1,sayi2):
        return sayi1+sayi2
    
    def cikar(self,sayi1,sayi2):
        return sayi1-sayi2
    
    def carp(self,sayi1,sayi2):
        return sayi1*sayi2

    def bol(self,sayi1,sayi2):
        return sayi1/sayi2


maths = Maths()
print("Toplam = " + str(maths.topla(2,78)))





#%% basics
# class Matematik:
#     def __init__(self,sayi1,sayi2):
#         self.sayi1 = sayi1
#         self.sayi2 = sayi2
#     def topla(self):
#         return self.sayi1 + self.sayi2

#     def cikar(self):
#         return self.sayi1 - self.sayi2

#     def carp(self):
#         return self.sayi1 * self.sayi2

#     def bol(self):
#         return self.sayi1 / self.sayi2

# matematik = Matematik(2,78)
# matematik2 = Matematik(3,76)
# print("Toplam = " + str(matematik.topla()))

#%%property
class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age


person1 = Person("Engin","Demiroğ",33)

print(person1.firstName)

class Worker(Person):
    def __init__(self,salary):
        self.salary = salary
        
    
    def logger1(self):
        print(self.firstName,self.lastName,self.salary)

        

class Customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
        


ahmet2 = Worker(2000)
ahmet2.firstName = "Ahmet"
ahmet2.lastName = "Demir"
ahmet2.age = 25



ahmet2.logger1()

# mehmet = Customer()

#%%

class Person:
    def __init__(self,name,surname,age,salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
 
    def logger(self):
        print(self.name, self.surname, self.age, self.salary)
 
class Employee(Person):
    def __init__(self,name,surname,age,salary):
        super().__init__(name,surname,age,salary)
 
a = Employee("Ahmet","Demir",28,3000)
a.logger()

# %%
