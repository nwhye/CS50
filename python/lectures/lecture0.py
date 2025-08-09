print("what is the name of the kitty?")
# or another way
input("what is the name of the kitty? ")
print("mewo, kitty")
# to run command it is possible to write command in terminal like python lecture0.py

"""
# remove whitespace from str (THOSE ARE CALLED METHODS)
name = name.strip()
# capitalize input as title, every words
name = name.title()
#  it can be done in one line
name = name.strip().title()
# OR
"""

# save answer = create variable - box that store value
name = input("what is the name of the kitty? ").strip().title()

print("mewo, kitty-" + name)  # to add value to the argument
print("mewo, kitty-", name)  # to separate arguments
# or
print("mewo, kitty-", end="")
print(name)
# or
print("mewo, kitty", name, sep="-")

# how to print quotes
print("mewo \"mewowo\"")
# or
print('mewo "mewowo"')

"""
everything inside is the comment
"""

# THE RIGHT WAY TO PRINT USER INPUT
print(f"mewo, kitty-{name}")

# split first and last name
first, last = name.split(" ")

print(f"owowo, mewo, kitty-{last}")

# to turn on interactive mode write in terminal 'python'


# --- CALCULATOR

x = input("What is x? ")
y = input("What is y? ")

z = int(x) + int(y)  # method to convert from str to int

print(z)

# we don't need to introduce new variable if we gonna use it once, so

x = int(input("What is x? "))
y = int(input("What is y? "))

print(x + y)

# convert to float, so it will support .0

x = float(input("What is x? "))
y = float(input("What is y? "))

print(round(x + y))  # to round answer

z = round(x + y, 2)  # so it will round to 2 digits after comma

print(f"{z:,}")  # if the user sum more than a 1000, so it will put in the answer comma (1,000)

print(f"{z:.2f}")  # so it will round to 2 digits after comma thorough format string


# --- CREATION OF OWN FUNCTIONS (def-define)

# def hello(to="kitty"):  # "kitty" would be written if there is no argument
#     print("hewwo", to)


# hello()  # no argument, so will be "kitty"
# hello(name)


# --- THE LOOK OF THE CODE
# functions can be all at the bottom of the screen, and action in the main. And in the end just call function main

# global variables that you want to use in any function must be in the beginning of the code, so at the top
eheh = ":>"


def main():
    global eheh  # use global so we can change things in variable
    eheh = ":<"
    # to call function inside function
    kittyname = get_name()  # we must declare the result of the called function
    print(kittyname)  # now print the declared variable with the result of the called function
    print("Uwu, "+kittyname)  # so in the beginning would be uwu

    f = int(input("what is f? "))
    print("f squared is equal to", square(f))


def get_name():
    kittyname = input("what is the name of the kitty? ")  # variables defined in the one can only used in this one func
    hello(kittyname)
    return kittyname


def hello(to="kitty"):  # "kitty" would be written if there is no argument
    print("hewwo", to)


def square(n):
    return n ** 2  # the same as n*n or pow(n,2)


main()  # to call main and use everything in the code
