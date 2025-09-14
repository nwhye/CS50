# --- Object-Oriented Programming

# as we already know
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")


def get_name():
    return input("Enter your name: ")


def get_house():
    return input("Enter your house: ")


if __name__ == "__main__":
    main()

# --- TUPLE - collection of data x,y and etc


def main():
    name, house = get_student()
    print(f"{name} from {house}")


def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return (name, house)  # return a tuple, in which 2 values (can be without brackets)
# tuple - immutable
# immutable - can not change the value
# list and dic are mutable


if __name__ == "__main__":
    main()


# so we can NOT unpack values from the tuple and give separate names:

def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


# fixing user input, but we must use list, and not tuple

def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return [name, house]


# let's optimize so when we have more than 2 value it would be easier to manage

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {}
    student["name"] = input("Enter your name: ")
    student["house"] = input("Enter your house: ")
    return student

# or


def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return {"name": name, "house": house}


# --- CLASSES AND OBJECTS
# class - blueprint, allows us to create our own data type (to define custom containers for pieces of data)
# primary feature of OOP is to be able to create your own objects

# when you use class you create OBJECTS (or instance)
# .name and .house here are attributes

class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()  # creating an object
    student.name = input("Enter your name: ")
    student.house = input("Enter your house: ")
    return student

# however it's reckless to put anything you want inside of object
# here the example with more control, as we're passing specific thing in to the class


def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    student = Student(name, house)  # working as a constructor
    return student

# --- CLASS (INSTANCE) METHODS

# let's fix things in class
# they come with certain METHODS

# object is an instance of the class

# self - represents the instance of the class being used
# instance - variable belonging to one and only one object


class Student:
    def __init__(self, name, house):  # dander init method - instance method, to initialize contents of the objects and
        # objects itself
        #                   ^ adding variables to objects
        # self is like the access to the current object that was created, place where variables stored
        self.name = name  # instance variable, can be .n .h, but it's less readable
        self.house = house  # there can be stored list, and not only variable


# we make variables inside the object and assign inside

# --- RAISE
# to create and raise your own exception when something goes wrong
# to alert that there is an error

# now we can control what's going inside the class. While in dictionary we can put anything

class Student:
    def __init__(self, name, house):
        # to raise an error:
        if not name:
            raise ValueError("Student name cannot be empty")
        if house not in ["gry", "hu", "rav", "sly"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    # to catch error:
    try:
        return Student(name, house)
    except ValueError:
        ...

# --- __str__
# method so any time someone calls object it will be shown as a string, and not address

class Student:
    def __init__(self, name, house):
        # to raise an error:
        if not name:
            raise ValueError("Student name cannot be empty")
        if house not in ["gry", "hu", "rav", "sly"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"Student {self.name} from {self.house}"


def main():
    student = get_student()
    print(student)

# --- OWN METHODS


class Student:
    def __init__(self, name, house, patronus):
        # to raise an error:
        if not name:
            raise ValueError("Student name cannot be empty")
        if house not in ["gry", "hu", "rav", "sly"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"Student {self.name} from {self.house}"

# our method
    def charms(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Russel terrier ":
                return "🐕"
            case _:
                return "🪄"


def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    patronus = input("Enter your patronus: ")
    # to catch error:
    try:
        return Student(name, house, patronus)
    except ValueError:
        ...


def main():
    student = get_student()
    print("Expecto Patronum")
    print(student.charm())


# --- PROPERTIES
# attribute with more defence mechanism, to prevent programmers to mess things up
# @property is to decorate functions
# decorators - functions that modify the behaviour of other functions

# property (fancy attribute(function)) called "house" and instance variable "_house"
# so when we return variable we print "return self.house"


class Student:

    def __init__(self, name, house):
        self.name = name
        self.house = house  # THIS LINE ALSO CALLS THE SETTER

    def __str__(self):
        return f"Student {self.name} from {self.house}"

# functions or in this case methods inside of class

# GETTER - function for a class to that gets some attribute
# @property to treat it as a getter
    @property
    def house(self):
        return self._house  # _house - instance variable

# SETTER - function in a class that sets some value
# now what to do to prevent setting invalid value
# called when trying to = to the object (student.house = "pepepoopoo") and anything ".house"
# so it is checking and not allowing, and raising ValueError
# @house.setter to treat it as a setter

# so no blind assignment from left to right, and if you try, it is checking class for setter

# !!! if you have instance variables "house" you can't call function "house"
    @house.setter
    def house(self, house):
        if house not in ["gry", "hu", "rav", "sly"]:
            raise ValueError("Invalid house")
        self._house = house

# so in order to access/set some attribute you go through some functions

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Student name cannot be empty")


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")

# _ means (by convention) private and "please, don't touch it"

# int str are classes, and .lower, .strip - methods that pre-build in the class

# dict() and {} are the same
# list() and [] are the same

# --- CLASS METHODS

# to create action that associated with the class, no matter what the objects
# @classmethod - it doesn't have access to self, but know what's class it's inside
# so bound to the class, and not the instance of the class


# sometimes we don't need many objects, and need only one
# so we can use Class as a container, for data and/or functionalty

# here the example how we would do it, but WITHOUT class method
import random


class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))


hat = Hat()
hat.sort("Harry")


# now let's do it the right way
# class variable - variable that exist in the class and there one copy for all objects
# we use it when we need to work with class, and not with objects

# so we don't need multiple hats, only one
# so, we use class as container to bundle functionality that connected to the hat

class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):  # cls - reference to the class
        print(name, "is in", random.choice(cls.houses))


# we are not bothered creating object, we just access class method inside the class
Hat.sort("Harry")
