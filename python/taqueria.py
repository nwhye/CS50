def main():

    menu = {
        "Baja Taco":4.25,
        "Burrito":7.50,
        "Bowl":8.50,
        "Nachos":11.00,
        "Quesadilla":8.50,
        "Super Burrito":8.50,
        "Super Quesadilla":9.50,
        "Taco":3.00,
        "Tortilla Salad":8.00,
    }


    total = float(0)
    while True:
        try:
            p = input("Item: ").title()
            if p in menu:
                total += menu[p]
                print(f"Total: ${total:.2f}")  # round to 2 deciamls
                continue
        except EOFError:  # for ctrl+d to stop the input
            print("")
            break
        except KeyError:
            pass


main()
