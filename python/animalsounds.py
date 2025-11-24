# Base class
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

# Derived class Dog
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

# Derived class Cat
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Derived class Bird
class Bird(Animal):
    def make_sound(self):
        print("Chirp! Chirp!")

# Demonstrating polymorphism
def animal_sound(animal):
    animal.make_sound()

# Create instances
dog = Dog()
cat = Cat()
bird = Bird()

# Call the function with different animals
animal_sound(dog)   # Woof! Woof!
animal_sound(cat)   # Meow!
animal_sound(bird)  # Chirp! Chirp!
