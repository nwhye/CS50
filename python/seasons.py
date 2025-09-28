import sys
import inflect
from datetime import date


class Born:
    def __init__(self, birthdate):
        self.birthdate = birthdate


    @staticmethod
    def validate(birthdate):
        try:
            check = date.fromisoformat(birthdate)
            return check
        except ValueError:
            sys.exit("Invalid date")


    @staticmethod
    def calculate(birthdate):
        today = date.today()
        difference = today - birthdate
        return difference.days * 24 * 60


    @staticmethod
    def convert(numbers):
        p = inflect.engine()
        text = p.number_to_words(numbers, andword="")
        return text.capitalize() + " minutes"


def main():
    birthdate = Born.validate(input("Date of Birth: "))
    difference = Born.calculate(birthdate)
    output = Born.convert(difference)
    print(output)


if __name__ == "__main__":
    main()
