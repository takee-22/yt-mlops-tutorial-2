#initiate a class
class Employee:
    #special method/magic method/dunder method - constructor

    def __init__(self):
         print('Started')
         self.id = 123
         self.salary = 50000
         self.designation = 'SDE'
         print("ended") 


    def travel(self,destination):
         print(f'Employee is travelling to {destination}')


#create an object/instance of the class
#sam = Employee()

 
#print(sam.salary)
#sam.travel("Barishal")

#print(type(sam))
a = 'x'
b = 'y'
