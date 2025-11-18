class dog:
    def speak(self):
        print("dog says woof! woof!")
class cat:
    def speak(self):
        print("cat says meow! meow!")
animals=[dog(),cat()]

for animal in animals:
    animal.speak()