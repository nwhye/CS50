# --- TRY and EXCEPT
while True:
    try:
        x = int(input("Enter a number: "))  # so if the user write str, it will go to exception
        # and through NameError as in right part int, and we're trying to put str.
    except ValueError:  # what to do when in this case it's not a number. and will go back to try as it is in the loop
        print("x is not an integer")
    else:
        break  # without else would be NameError, and now there is condition to make after good "try"

print(f"x is {x}")  # when finally receive correct answer, break out of the loop and execute

# another version

while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")

# return is to handle back something, and not just print
# continue is to go to next cycle of while true loop

# we can do it as a function and make it shorter

# except EOFError:  # for ctrl+d to stop the input
# print("")
# break


# --- PASS
# catch error, but passing on saying anything

while True:
    try:
        x = int(input("Enter a number: "))
    except ValueError:
        pass  # so it will ask answer again, without showing any errors, till it get right answer
    else:
        break

print(f"x is {x}")

# --- FINAL VERSION


def main():
    x = get_int("What's the x? ")
    print(f"x is {x}")


def get_int(prompt):  # we can send anything, just calling it's prompt as it's what we want
    while True:
        try:
            return int(input(prompt))  # return is to handle back something, and not just print.
            # and can break out of the loop. also we don't really need variable if we use it right line down.

            # !!! prompt, as we asked it in main, when we called a function, and passed as ARGUMENT here.

        except ValueError:
            print("x is not an integer")


main()

# --- COOL STUFF

def main():
    f = fuel_check("Fraction: ")
    print(f)

def fuel_check(fraction):
    while True:
        try:
            x, y = input(fraction).split("/")
            x = int(x)
            y = int(y)
            if x > y:
                continue  # go to next cycle of while true loop
            if x<0 or y<0:
                continue

            fuel = int(round(x/y * 100))
            if fuel >= 99:
                return("F")
            elif fuel <= 1:
                return("E")
            else:
                return(f"{fuel}%")

        except (ValueError, ZeroDivisionError):
            pass

main()
