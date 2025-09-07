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
    print(f"{student['name']} from {student['student']}")


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


