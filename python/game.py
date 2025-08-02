import random

while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            continue
        else:
            break
    except ValueError:
        continue

while True:
    try:
        number = random.randint(1, level)
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
        else:
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                break
    except ValueError:
        continue

