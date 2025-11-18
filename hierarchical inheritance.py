class food_shop:
    def eat(self):
        print("the food is eating")
class meat(food_shop):
    def stop(self):
        print("the stop to eat")
class fish(food_shop):
    def start(self):
        print("ok you start eating food")
m=meat()
f=fish()

m.eat()
m.stop()

f.eat()
f.start() 