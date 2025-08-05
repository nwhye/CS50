def main():
    while True:
        try:
            f = convert("Fraction: ")
            percent = gauge(f)
            print(percent)
            break

        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = input(fraction).split("/")
    x = int(x)
    y = int(y)
    if x > y:
        raise ValueError
    if x<0 or y<0:
        raise ValueError

    return round(x/y * 100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
