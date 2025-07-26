def main():
    coins = int(50)
    print("Amount Due: " + str(coins))

    while coins > 0:
        in_coins = int(input("Insert Coins: "))
        if in_coins==25:
            coins -= 25
        elif in_coins==10:
            coins -= 10
        elif in_coins==5:
            coins -= 5

        if coins > 0:
            print("Amount Due: " + str(coins))
        elif coins <= 0:
            print("Change Owed: " + str(coins).strip("-"))


main()
