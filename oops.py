

    #OOPS
class employee:
    company_name = 'ABC Company'
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def show(self):
        print('employee:',self.name,self.salary, self.company_name)

emp1 = employee("harry",34666)
emp1.show()
    
emp2 = employee("rahul",346788)
emp2.show()
        



#childclass
class vehicle:
   def __init__(self,name,max_speed,mileage):
       self.name=name
       self.max_speed=max_speed
       self.mileage= mileage
       
        
    