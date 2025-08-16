import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    valid = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)
    values = ip.split(".")
    if valid:
        for i in values:
            if int(i) > 255 or (i.startswith("0") and len(i) > 1):
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
