from validator_collection import checkers

address = checkers.is_email(input("Email: "))

if address == True:
    print("Valid")
else:
    print("Invalid")

