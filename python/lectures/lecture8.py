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

