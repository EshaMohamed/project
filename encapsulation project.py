class employee:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
    @property
    def salary(self):       #getter
        return self.__salary
    @salary.setter
    def salary(self,amount):        #setter
        if amount>=15000:
            self.__salary=amount
        else:
            print("amount is empty")
emp1=employee("eshamohamed",12000)
print(emp1.salary)

emp1.salary=10000
print(emp1.salary)

emp1.salary=20000
print(emp1.salary)