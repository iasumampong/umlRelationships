class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

my_dog = Dog("Buddy")

print(my_dog.name)
print(my_dog.make_sound())