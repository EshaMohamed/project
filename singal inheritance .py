class parent:
    def parent_method(self):
        print("this is parent method")
class child(parent):
    def child_method(self):
        print("this is child method")
x=child()
x.parent_method()
x.child_method()