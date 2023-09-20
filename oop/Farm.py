class Creature:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"

    def say(self, sound):
        return f"{self.name} says {sound}"

    def walk(self):
        return f"{self.name} is walking"


# class Animal that inherits from Creature
class Animal(Creature):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def make_milk(self):
        return f"{self.name} makes a milk"

    def sleep(self):
        return f"{self.name} is sleeping"


# class Bird that inherits from Creature
class Bird(Creature):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def fly(self):
        return f"{self.name} is flying"

    def croaks(self):
        return f"{self.name} is croaking too much"


# class Dog that inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def run(self):
        return f"{self.name} is running for a ball"

    def bark(self):
        return f"{self.name} is barking"


# class Duck that inherits from Bird
class Duck(Bird):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.species = "Duck"

    def swim(self):
        return f"{self.name} is swimming"

    def quack(self):
        return f"{self.name} says quack"

    def drink(self):
        return f"{self.name} is drinking water"


# farm animals and birds
cow = Animal("Milk", "Cow")
crow = Bird("Brilliant", "crow")
french_bulldog = Dog("Chop", "French Bulldog")
duck = Duck("Daffy", "Duck")

# the methods of these farm inhabitants
print(cow)
print(cow.say("Moo"))
print(cow.walk())
print(cow.make_milk())
print(cow.sleep())

print(crow)
print(crow.say("Caw"))
print(crow.walk())
print(crow.fly())
print(crow.croaks())

print(french_bulldog)
print(french_bulldog.say("Woof"))
print(french_bulldog.walk())
print(french_bulldog.run())
print(french_bulldog.bark())

print(duck)
print(duck.say("Quack"))
print(duck.walk())
print(duck.swim())
print(duck.drink())
