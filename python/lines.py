import sys

def main():
    try:
        code_name = sys.argv[1]
        if len(sys.argv) > 2:
            sys.exit("Too many comand line arguments")
        elif code_name[-3:] != ".py":
            sys.exit("Not a python file")

    except IndexError:
        if len(sys.argv) <= 1:
            sys.exit("Too few comand line arguments")

    try:
        with open(code_name, "r") as file:
            line_counter = 0
            for line in file:
                strip = line.lstrip()
                if strip.startswith("#") or strip == "":
                    continue
                line_counter += 1
            print(line_counter)

    except FileNotFoundError:
        sys.exit("File does not exist")

main()
