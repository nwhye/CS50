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


if __name__ == "__main__":
    main()


# so we can NOT unpack values from the tuple and give separate names:

def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")