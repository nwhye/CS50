# LOOP
i = 3
while i != 0:
    print("meow")
    i = i - 1

a = 1
while a <= 3:
    print("meow")
    a = a + 1

# better
b = 0
while b < 3:
    print("meow")
    b += 1

# FOR
for i in [0, 1, 2]:
    print("meow")

# better!
for _ in range(3):  # _ is meaning that we're not using it in the future and don't care about the name
    print("meow")

# 0o0
print("meow\n" * 3, end="")

# cool thing
# if n < 0:
#     continue
# else:
#     break

# VALIDATING INPUT
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

# HOW TO USE


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n  # even if you break out of the loop, you must return something


def meow(n):
    for _ in range(n):
        print("meow")


main()

# LIST
students = ["Danya", "Anya", "Artem"]

print(students[0])

for student in students:  # instead of "student" can be just "s"
    print(student)

for i in range(len(students)):  # to show the number of the content in list ( 1 Danya 2 Anya 3 Artem)
    # we use len(students) so we can dynamically change the size of list, and this loop still will be working
    print(i + 1, students[i])  # +1 to hide that we're counting from 0

# DICTIONARY (keys and values)

friends = {
    "Danya": "Cool",
    "Anya": "not cool",
    "Artem": "not cool"
}

print(friends["Danya"])  # so it will print Cool, the value in dictionary

for fri in friends:
    print(fri)  # we only see keys - Danya, Anya, Artem

for fri in friends:
    print(fri, friends[fri], sep=", ")  # to take keys and values. and separator to put comma and space


# good use of dictionary
def main():
    shopping_list = {}

    while True:
        try:
            x = input("").upper()
            if x in shopping_list:
                shopping_list[x] += 1
            else:
                shopping_list[x] = 1
        except EOFError:
            for _ in sorted(shopping_list):
                print(shopping_list[_], _)
            break
        except KeyError:
            pass
        except NameError:
            pass


main()


# LIST OF DICTIONARIES

friends = [
    {"name": "Danya", "age": 19, "status": "cool"},
    {"name": "Anya", "age": 23, "status": "not cool"},
    {"name": "Artem", "age": 21, "status": None}  # None is an absence of the value
]

for fri in friends:
    print(fri["name"], fri["age"],  sep=", ")  # to print names and age. fri = keys in dictionary


# NESTED LOOPS

for _ in range(3):
    print("#")


def main():
    print_column(3)
    print_row(4)

    print_square(3)


def print_column(height):  # can be just n
    # for _ in range(height):
    #     print("#")

    print("#\n" * height, end="")  # another solution to print "#" in a column


def print_row(width):
    print("?" * width)  # to print ????


def print_square(size):
    for i in range(size):  # to each row in square
        for j in range(size):  # to each brick in square
            print("#", end="")  # print brick
        print()  # to print new line at the end of the row


def print_square2(size):
    for i in range(size):
        print("#" * size)  # same solution, fewer lines


# or

def print_square3(size):
    for i in range(size):
        print_row(size)