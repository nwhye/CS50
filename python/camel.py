def main():
    camel = input("camelCase: ")
    snake = ""

    for c in camel:
        if c.isupper():
            snake += "_" + c.lower()  # adding lowered cases and before it _, and then update "snake"
        else:
            snake += c

    print("snake_case: " + snake)

main()
