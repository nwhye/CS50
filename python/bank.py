def main():
    txt = input("Greetings: ").strip()
    greet = value(txt)
    print(f"${greet}")


def value(greeting):
    if greeting.startswith("Hello"):
        return int(0)
    elif greeting.startswith("H"):
        return int(20)
    else:
        return int(100)


if __name__ == "__main__":
    main()
