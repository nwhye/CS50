def main():
    plate = input("Plate: ")
    if is_valid(plate):  # sending box
        print("Valid")
    else:
        print("Invalid")

def is_valid(arg1):  # box with the plate. just an argument. the order matters.

    if len(arg1) > 6:
        return False

    letter_count = 0
    for p in arg1:
        if p.isdigit():
            break
        else:
            letter_count += 1

    if letter_count>=2:
        l_plate = arg1[0:letter_count]
        n_plate = arg1[letter_count:6]

    else:
        return False

    if n_plate == "":
        return True

    if not n_plate.isdigit():
        return False

    if not l_plate.isalpha():
        return False

    if n_plate[0]=="0":
        return False

    return True

main()
