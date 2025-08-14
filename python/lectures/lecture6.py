# --- FILE I/O

# add user input ot the list
names = []

for _ in range(3):
    name = input("What's your name?" )
    names.append(name)

# OR BETTER

for _ in range(3):
    names.append(input("What's your name?" ))

# print sorted version of this list
for name in sorted(names):
    print(f"hello, {name}")


# --- OPEN - like a double click (name of file and how to open)

name = input("What's your name?" )

file = open("names.txt", "w")  # w - create file also re-create
file.write(name)  # now we write input "name"
file.close()  # save and close
# This program only saves the last input, because of "w"

# To add, we need to APPEND - A
file = open("names.txt", "a")
file.write(f"{name}\n")  # without n it would stack
file.close()

# Better design, more pytonic and automatic, that will auto close file

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# --- HOW TO READ FILE

with open("names.txt", "r") as file:   # r - read
    lines = file.readlines()  # read and return all lines from the file, storing it in var "lines"

for line in lines:
    print("hello,", line.rstrip())  # delete new line, so there is no empty lines between printed lines


# better look, but we can't sort it
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())


# --- Now let's sort it

names = []

# we should read, striping it
with open("names.txt") as file:
    for line in file:  # iterate
        names.append(line.rstrip())  # not print, but add to the list, and strip new line

# after we load it in memory , we can sort and show, that located in memory
for name in sorted(names):  # loop in sorted names
    print(f"hello, {name}")  #


# --- HOWEVER, if we want just to sort file and print (not doing any changes to the file):

with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())

# --- CSV - comma-separated values
# to store multiple information, that related to each other in one file
# separate it with comma and diff types of values with new line (Danya,cool \n Anya,not cool)

# code to read csv files

with open("names.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is {row[1]}")  # Danya is cool \n Anya is not cool

# now make it easier to read

with open("names.csv") as file:
    for line in file:
        name, status = line.rstrip().split(",")  # because we separate content, so we can assign 2 variables
        print(f"{name} is {status}")  # Danya is cool \n Anya is not cool


# now let's sort it and print sorted version (sloppy version)
names = []
with open("names.csv") as file:
    for line in file:
        name, status = line.rstrip().split(",")
        names.append(f"{name} is {status}")  # names - name of the created list

for names in sorted(names):
    print(f"hello, {names}")


# well designed version +
# --- SORT KEYS
names = []
with open("names.csv") as file:
    for line in file:
        name, status = line.rstrip().split(",")
        person = {"name": name, "status": status}  # dictionary where we create keys and values and assign using var
        names.append(person)  # handling to the list particular name


def get_name(pe):  # function to return the name of the person from the dictionary (alphabetic)
    return person["name"]


def get_status(pe):  # function to sort by status (alphabetic)
    return person["status"]


for name in sorted(names, key=get_name):  # passing in func. sorted key-function, that will sort by name
    print(f"{person['name']} is {person['status']}")  # calling from dictionary with specific keys


# but how to tight this code even more?
# --- LAMBDA FUNCTIONS
# anonymous function, that you call once, so why create separate function and give it a name

names = []
with open("names.csv") as file:
    for line in file:
        name, status = line.rstrip().split(",")
        person = {"name": name, "status": status}
        names.append(person)

for name in sorted(names, key=lambda pe: person["name"]):  # functiona called on every "pe" in the list
    # pe - name of the parameter to take(can be called anything)
    # person - dictionary where we're searching, accessing the "name"
    # for every pe in person we take (and later sort) by name
    print(f"{person['name']} is {person['status']}")


# --- CSV LIBRARY
# READER
# in module csv exist function reader, to read the file for you, and deside where commas
import csv

names = []
with open("names.csv") as file:
    reader = csv.reader(file)  # "file" is an input that we pass to the csv.reader
    # in dic choosing list with index 0
    '''for row in reader:
        names.append({"name": row[0], "status": row[1]})   
    '''
    # easier way, if we know the amount of values, we can define it
    for name, status in reader:
        names.append({"name": name, "status": status})

for name in sorted(names, key=lambda pe: person["name"]):
    print(f"{person['name']} is {person['status']}")


# --- DICT READER

# we can make csv file have "name" and "status" printed inside, so we don't need to name it in code
# now we can use DictReader, and not just reader, and make everything more flexible
'''
name,status,home
Danya,cool,"Kyiv, Ukraine"
Anya,not cool,"Minsk, Belarus"
'''
import csv

names = []

with open("names.csv") as file:
    reader = csv.DictReader(file)  # now it's loading it not as list of columns, but as dictionary of columns
    for row in reader:  # row as we already now there are keys in csv
        names.append({"name": row["name"], "status": ["status"]})
        # or just say names.append(row) but i don't understand why

for name in sorted(names, key=lambda pe: person["name"]):
    print(f"{person['name']} is {person['status']}")

# so now even if the columns inside csv file were appended and added, it's still will use "name" and "status"


# --- CSV WRITER

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

# however we can do it better, without worrying about the order
# because we're passing the list, and not dic


# --- DICT WRITER

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])  # fieldnames - order in which they would be
    writer.writerow({"name": name, "home": home})  # passing in which column goes which data
    # they can be switched, and we can write home then name, but it will fill in order of "fieldnames"


# --- PIL
# library to navigate images
# lets use 2 images to make gif, that we passing through command line
# but it can be more, just should print the name

# python animation.py frame1.gif frame2.gif
# and then code animation.py  - to open

import sys

from PIL import Image

images = []  # to accumulate all images

# this block to iterate over passed arguments and open files
for arg in sys.argv[1:]:  # take file names from the command line and take it as an arguments
    # also we made slice, from first index and to the end
    image = Image.open(arg)  # passing to the function "image.open" argument
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
# 1. name of the gif, 2. save all passed to the functions   frames, 3. to the [0] we append the list of images,
# in our case only [1] (images[1] meaning the next images), 4. duration of each frame in ms,
# 5. loop forever, 0 - infinit


# --- WAY TO CHECK ARGUMENTS

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

before_file = sys.argv[1]
after_file = sys.argv[2]

if not before_file.endswith(".csv") or not after_file.endswith(".csv"):
    sys.exit("Files must be CSV format")