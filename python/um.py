import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um = re.findall(r"(^| )um(,| |$|\?|\.)", s, re.IGNORECASE)
    um_len = len(um)
    return um_len


if __name__ == "__main__":
    main()
