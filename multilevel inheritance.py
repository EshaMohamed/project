class car:
    def tata(self):
        print("this is tata car")
class bike(car):
    def hero(self):
        print("this is hero bike")
class cycle(bike):
    def super(self):
        print("this is super cycle")
x=cycle()
x.tata()
x.hero()
x.super()