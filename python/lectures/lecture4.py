# modules is a library with functions or other build in features


# program to generate
# import random. we import everything, but what if we want to use just choice, and not write "random.choice" every time?
# from random import choice
import random

coin = random.choice(["heads", "tails"])
print(coin)

# return random integer from this range
number = random.randint(1, 10)
print(number)

# shuffle arguments in place (list)
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:  # loop to print one by one
    print(card)

# average
import statistics

print(statistics.mean([100, 90]))

# COMMAND-LINE ARGUMENTS
# SYS.ARGV
# after "python name.py " type something as an input
# without arguments - IndexError
# if in line we write name and surname in "Hanna A" it will pass as one argument. But Hanna A as 2

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is ", sys.argv[1]) # take input in the command line, when calling program.
    # [1] - because sys.argv store the name of the program as 0

# mature way to handle if else, is to not hide real code in else

if len(sys.argv) < 2:
    sys.exit("Too few arguments")  # exit program
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is ", sys.argv[1])


# MULTIPLE INPUT
# SLICE

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:                  # to iterate over the list (can be "name", not "arg")
    # [1:] from first index in list - slice of the list
    # [1:-1] remove last ("counting in the other direction from the end of the list")
    print("hello, my name is ", arg)


# PACKAGES
# to install 3rd parties libraries
# PyPI - pypi.org - to install any type of packages

# pip - package manager, to install package/lib
# pip install cowsay

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])  # there would be drawn cow and saying your name
    cowsay.trex("hello, " + sys.argv[1])

# there is only if, so nothing happened until conditions are met


# API
# API application programming interface, referred to 3rd parties services
# it can connect to the data on the server and work together with your code

# pip install requests

# JSON javascript object notation = to exchange data between computers

# code to use itunes API
import requests
import json  # to manipulate json file and in our case format it

if len(sys.argv) != 2:  # if there is no name of the band inputed
    sys.exit()

# program to pretend to be browser to access http
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# after = can add any band name that was inputted
print(json.dumps(response.json(), indent=2))  # showing the content as a json and converting to python dic
# json.dumps - pretty printing and indent=2  refers to the spaces at the beginning of a code line


# code to iterate all songs of the inputted group (show 50)

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])  # change 1 to 50
print(json.dumps(response.json(), indent=2))

o = response.json()

for result in o["results"]:  # loop to iterate all songs of the inputted group
    # "results is a key inside dictionary response that we got in previous code"
    print(result["TrackName"])  # and it's going to chow TrackName, another key that we got earlier
    # these names we got from the itunes API, and those JSON things we can not change


# YOUR OWN LIBRARY

# ----------------------------------
# file "saying.py"
def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"Hello {name}")


def goodbye(name):
    print(f"Good bye, {name}")


main()


# -----------------------------------
# now in another file "say.py"

import sys
from sayings import hello  # to import just the hello function from out file "sayings.py"

if len(sys.argv) == 2:
    hello(sys.argv[1])


# main going to be called in another file, no matter what.

# so at the end of saying.py we must write

if __name__ == "__main__":
    main()

# so it's checking if the code main called from this file, or imported.
# If its imported the main in "saying.py" not called