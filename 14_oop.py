# ============================================================
#  PYTHON COURSE — Chapter 14: Object-Oriented Programming
# ============================================================
# OOP organises code around OBJECTS instead of functions.
# An object = data (attributes) + behaviour (methods).
#
# 4 Pillars of OOP:
#  1. Encapsulation  — bundle data + methods, hide internals
#  2. Inheritance    — child class reuses parent class code
#  3. Polymorphism   — same method name, different behaviour
#  4. Abstraction    — show only what's necessary, hide details
# ============================================================


# ════════════════════════════════════════════════════════════
#  1. CLASSES & OBJECTS
# ════════════════════════════════════════════════════════════
# A CLASS is a blueprint. An OBJECT is a created instance.
# class ClassName:
#     attributes and methods

class Factory:
    # Class attribute — shared by ALL objects of this class
    company = "Coding Academy Ltd."

    def greet(self):    # self → refers to the calling object
        print(f"Hello from {Factory.company}")

obj1 = Factory()   # create object (instance)
obj2 = Factory()

obj1.greet()   # Hello from Coding Academy Ltd.
obj2.greet()   # same — both share the class attribute


# ════════════════════════════════════════════════════════════
#  2. __init__ — CONSTRUCTOR
# ════════════════════════════════════════════════════════════
# __init__ runs AUTOMATICALLY when an object is created.
# Use it to set initial values (instance attributes).

class Factory:
    def __init__(self, material, zips, pockets):
        # instance attributes — unique to each object
        self.material = material
        self.zips     = zips
        self.pockets  = pockets

    def show(self):
        print(f"Material: {self.material} | Zips: {self.zips} | Pockets: {self.pockets}")

reebok = Factory("Leather", 3, 2)   # creates one object
campus = Factory("Nylon",   3, 3)   # creates another with different data

reebok.show()
campus.show()


# ════════════════════════════════════════════════════════════
#  3. TYPES OF METHODS
# ════════════════════════════════════════════════════════════

class Animal:
    # Class attribute
    kingdom = "Animalia"

    def __init__(self, name, age):
        self.name = name    # instance attribute
        self.age  = age

    # Instance method — works with instance data (self)
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

    # Class method — works with class data (cls), not instance
    @classmethod
    def get_kingdom(cls):
        print(f"Kingdom: {cls.kingdom}")

    # Static method — no access to class or instance data
    # Just a utility function that lives inside the class
    @staticmethod
    def breathes():
        print("All animals breathe oxygen.")

lion = Animal("Lion", 5)
lion.show()             # instance method
Animal.get_kingdom()    # class method — called on class
Animal.breathes()       # static method — called on class


# ════════════════════════════════════════════════════════════
#  4. ENCAPSULATION — Hiding Internal Data
# ════════════════════════════════════════════════════════════
# Use __ (double underscore) prefix to make an attribute private.
# Private attributes are NOT accessible directly from outside.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner    = owner
        self.__balance = balance    # private — hidden from outside

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited ₹{amount}. Balance: ₹{self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("❌ Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"✅ Withdrawn ₹{amount}. Balance: ₹{self.__balance}")

    def get_balance(self):    # controlled access via a method (getter)
        return self.__balance

acc = BankAccount("Kamran", 1000)
acc.deposit(500)
acc.withdraw(200)
print(f"Balance: ₹{acc.get_balance()}")

# print(acc.__balance)   # ❌ AttributeError — private!


# ════════════════════════════════════════════════════════════
#  5. SINGLE INHERITANCE
# ════════════════════════════════════════════════════════════
# Child class inherits ALL attributes and methods of parent.
# Syntax: class Child(Parent):

class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} breathes oxygen.")

class Dog(Animal):   # Dog inherits from Animal
    def bark(self):
        print(f"{self.name} says: Woof! 🐕")

d = Dog("Bruno")
d.breathe()    # inherited from Animal
d.bark()       # defined in Dog


# ════════════════════════════════════════════════════════════
#  6. super() — Calling the Parent's __init__
# ════════════════════════════════════════════════════════════

class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name: {self.name}")

class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name)    # call Animal's __init__ to set self.name
        self.age = age            # add extra attribute

    def show(self):               # override the parent's show()
        print(f"Name: {self.name}, Age: {self.age}")

lion   = Animal("Lion")
person = Human("Kamran", 23)

lion.show()     # Name: Lion
person.show()   # Name: Kamran, Age: 23


# ════════════════════════════════════════════════════════════
#  7. MULTILEVEL INHERITANCE
# ════════════════════════════════════════════════════════════
# A → B → C  (chain of inheritance)

class Factory:
    def __init__(self, material, zips):
        self.material = material
        self.zips     = zips

class BhopalFactory(Factory):
    def __init__(self, material, zips, color):
        super().__init__(material, zips)
        self.color = color

class PuneFactory(BhopalFactory):
    def __init__(self, material, zips, color, pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets

    def show(self):
        print(f"Material: {self.material} | Zips: {self.zips} | "
              f"Color: {self.color} | Pockets: {self.pockets}")

p = PuneFactory("Denim", 2, "Blue", 4)
p.show()


# ════════════════════════════════════════════════════════════
#  8. MULTIPLE INHERITANCE
# ════════════════════════════════════════════════════════════
# A class can inherit from MORE than one parent.

class Flyer:
    def fly(self):
        print("I can fly ✈️")

class Swimmer:
    def swim(self):
        print("I can swim 🏊")

class Duck(Flyer, Swimmer):    # inherits from both
    def quack(self):
        print("Quack! 🦆")

d = Duck()
d.fly()    # from Flyer
d.swim()   # from Swimmer
d.quack()  # Duck's own method


# ════════════════════════════════════════════════════════════
#  9. POLYMORPHISM — Method Overriding
# ════════════════════════════════════════════════════════════
# The child class can OVERRIDE a method from the parent.
# Same method name → different behaviour per class.

class Shape:
    def area(self):
        print("Area not defined")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):    # overrides Shape.area()
        print(f"Square area: {self.side ** 2}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):    # overrides Shape.area()
        print(f"Circle area: {3.14 * self.radius ** 2:.2f}")

shapes = [Square(5), Circle(7), Square(3)]

for shape in shapes:
    shape.area()    # same call → different output per object ✅


# ════════════════════════════════════════════════════════════
#  10. ABSTRACTION — Abstract Classes
# ════════════════════════════════════════════════════════════
# An abstract class defines a BLUEPRINT that child classes MUST follow.
# You cannot create an object from an abstract class directly.
# Use @abstractmethod to force child classes to implement methods.

from abc import ABC, abstractmethod

class Shape(ABC):      # inherit from ABC to make it abstract
    @abstractmethod
    def area(self):
        pass           # no body — child MUST implement this

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

sq = Square(5)
ci = Circle(7)

print(f"Square — Area: {sq.area()}, Perimeter: {sq.perimeter()}")
print(f"Circle — Area: {ci.area():.2f}, Perimeter: {ci.perimeter():.2f}")

# shape = Shape()   # ❌ TypeError — can't instantiate abstract class


# ════════════════════════════════════════════════════════════
#  11. MAGIC / DUNDER METHODS
# ════════════════════════════════════════════════════════════
# Special methods with double underscores (__).
# Python calls them automatically in certain situations.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def __str__(self):
        # Called when you print(obj) or str(obj)
        return f"Animal(name={self.name}, age={self.age})"

    def __repr__(self):
        # Called in interactive shell / debugging
        return f"Animal('{self.name}', {self.age})"

    def __len__(self):
        # Called when len(obj) is used
        return self.age

    def __add__(self, other):
        # Called when you use + between two objects
        return Animal(f"{self.name}&{other.name}", self.age + other.age)

    def __eq__(self, other):
        # Called when == is used
        return self.name == other.name and self.age == other.age

lion    = Animal("Lion", 12)
dolphin = Animal("Dolphin", 14)

print(lion)             # uses __str__
print(repr(lion))       # uses __repr__
print(len(lion))        # uses __len__  → 12
combined = lion + dolphin  # uses __add__
print(combined)
print(lion == dolphin)  # uses __eq__ → False


# ════════════════════════════════════════════════════════════
#  12. @property — Getter & Setter
# ════════════════════════════════════════════════════════════
# @property lets you access a method like an attribute.
# Use it to add validation when getting or setting values.

class Circle:
    def __init__(self, radius):
        self._radius = radius    # _radius is "protected" by convention

    @property
    def radius(self):            # getter — access like: obj.radius
        return self._radius

    @radius.setter
    def radius(self, value):     # setter — called when: obj.radius = value
        if value < 0:
            raise ValueError("Radius cannot be negative!")
        self._radius = value

    @property
    def area(self):              # computed property — no setter needed
        return 3.14 * self._radius ** 2

c = Circle(5)
print(c.radius)    # 5      — uses getter
print(c.area)      # 78.5   — computed property

c.radius = 10      # uses setter — validates the value
print(c.radius)    # 10

# c.radius = -3    # ❌ ValueError — caught by setter


# ============================================================
#  Quick Recap — 4 Pillars
#  Encapsulation  → __ prefix hides data; use getters/setters
#  Inheritance    → class Child(Parent): — reuse parent code
#  Polymorphism   → override methods for different behaviour
#  Abstraction    → ABC + @abstractmethod = enforced blueprint
#
#  Key Concepts
#  __init__   → constructor (runs on object creation)
#  self       → reference to the current object
#  super()    → call parent's __init__ or methods
#  @classmethod → works with cls (class data)
#  @staticmethod → utility method, no self or cls
#  Dunder methods → __str__, __add__, __len__, __eq__ …
# ============================================================
