import sys
import csv
import tabulate

def main():
    try:
        file_name = sys.argv[1]
        if len(sys.argv) > 2:
            sys.exit("Too many comand line arguments")
        elif file_name[-4:] != ".csv":
            sys.exit("Not a csv file")

    except IndexError:
        if len(sys.argv) <= 1:
            sys.exit("Too few comand line arguments")

    try:
        with open(file_name) as file:
            reader = csv.DictReader(file)
            print(tabulate.tabulate(reader, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

main()
