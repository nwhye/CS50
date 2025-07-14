def main():
    txt = input("Gretings: ").strip()

    if txt.startswith("Hello"):
        print("$0")
    elif txt.startswith("H"):
        print("$20")
    else:
        print("$100")

main()
