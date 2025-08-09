# --- CONDITIONALS
x = int(input("Enter the number x: "))
y = int(input("Enter the number y: "))

if x < y:
    print("x is less than y")
# elif is when it receives true answer it stops. and if first if correct it will stop after first if
elif x > y:
    print("x is greater than y")
# else is when receive false answer for both questions. not question, just logical conclusion  
else:
    print("x is equal to y")


# another comparison
if x > y or x < y:
    print("x is not equal to y")
else:
    print("x is equal to y")


# better version!!!
if x != y:
    print("x is not equal to y") 
# or == and "x is equal to y"
else:
    print("x is equal to y")


# --- AND
score = int(input("Scroe:  "))

#instead of score >= 90 and score <=100
if 90 <= score <= 100:
    print("Grade: A")

# another solution:
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade F")


# --- % modular
x = int(input("What's x: "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# --- CLEAN VERSION
def main():
    x = int(input("What's x: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

#return True if n % 2 == 0 esle False

    return n % 2 == 0


name = input("What's your name? ")

#if name == "harry" or name == "hermione"

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryff")
    case "Draco":
        print("Slyth")  
    case _:
        print("Who?")

#to shorten some things it is possible to use IF NOT conditionals. if not (dif = difficut or dif = casual): print("be") return

main()
