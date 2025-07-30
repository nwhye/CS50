def main():
    shopping_list = {}

    while True:
        try:
            x = input("").upper()
            if x in shopping_list:
                shopping_list[x] += 1
            else:
                shopping_list[x] = 1
        except EOFError:
            for _ in sorted(shopping_list):
                print(shopping_list[_], _)
            break
        except KeyError:
            pass
        except NameError:
            pass


main()
