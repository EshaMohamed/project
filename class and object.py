class car:
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
        self.speed=0
        
    def display(self):
        print("NAME:",self.name)
        print("MODEL:",self.model)
        print("YEAR:",self.year)
        
    def accelerator_high(self,increase):
        self.speed += increase
        print(f"Accelerator.... current speed {self.speed} km/hr")
        
    def accelerator_low(self,decrease):
        self.speed -= decrease
        if self.speed<0:
            self.speed=0
        print(f"Acclerator is loww  current speed{self.speed} km/hr") 
    
car1=car("Esha","Tata",2025)
car2=car("Mohamed","Ford",2024)

car1.display()
car1.accelerator_high(50)
car1.accelerator_low(20)


car2.display()
car2.accelerator_high(60)
car2.accelerator_low(30)
