import random

def main():
    a = get_level()
    i = 1
    score = 0

    while i <= 10:
        try:
            x = generate_integer(a)
            y = generate_integer(a)
            correct_answer = x + y
            j = 1

            while j <= 3:
                answer = input(f"{x} + {y} = ")

                if not answer.isdigit() or (int(answer) != correct_answer):
                    print("EEE")
                    if j != 3:
                        j += 1
                    else:
                        print(f"{x} + {y} = {correct_answer}")
                        break
                elif int(answer) == correct_answer:
                    score += 1
                    break
            i += 1

        except EOFError:
            break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level<1 or level>3:
                continue
            else:
                return level
        except ValueError:
            continue


def generate_integer(level):  # level = amont of digits in math problems
    if level != 1:
        start = 10**(level-1)
    else:
        start = 0
    end = (10**level)-1
    return random.randint(start, end)


if __name__ == "__main__":
    main()
