class dad:
    def father(self):
        print("father is : driving")
class mom:
    def mother(self):
        print("mother is : cooking")
class child(dad,mom):
    def child(self):
        print("son is :  playing")
x=child()
x.child()
x.father()
x.mother()