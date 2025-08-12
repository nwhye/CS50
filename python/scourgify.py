import sys
import csv

def main():
    try:
        before_file = sys.argv[1]
        after_file = sys.argv[2]

        if len(sys.argv) > 3:
            sys.exit("Too many comand line arguments")
        elif before_file[-4:] != ".csv":
            sys.exit("Not a csv file")
        elif after_file[-4:] != ".csv":
            sys.exit("Not a csv file")

    except IndexError:
        if len(sys.argv) <= 1:
            sys.exit("Too few comand line arguments")

    try:
        with open(before_file, newline="") as file:
            reader = csv.DictReader(file)
            changed_rows = []  # create dict that we later append and write to the after_file
            for row in reader:
                last, first = row["name"].split(", ")  # the way to split the exact column in dict
                changed_rows.append({"first":first, "last":last, "house":row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {before_file}")

    try:
        with open(after_file, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()  # to write fieldnames
            writer.writerows(changed_rows)  # add dict that we created


    except FileNotFoundError:
        sys.exit(f"Could not read {after_file}")


if __name__ == "__main__":
    main()
