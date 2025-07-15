def main():
    n = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

    if n == "42" or n == "forty-two" or n == "forty two":
        print("Yes")
    else:
        print("No")


main()
