def main():
    f = fuel_check("Fraction: ")
    print(f)

def fuel_check(fraction):
    while True:
        try:
            x, y = input(fraction).split("/") # работает. делит.
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
