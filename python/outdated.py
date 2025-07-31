def main():
    m = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]


    while True:
        try:
            in_date = input("Date: ")
            # 09/12/2005 format
            if "/" in in_date:
                if any(c.isalpha() for c in in_date):
                    continue
                else:
                    month, day, year = map(int, in_date.split("/"))

                    if month > 12 or day > 31:
                        continue
                    else:
                        if month < 10:
                            month = (f"{month:02}")
                        if day < 10:
                            day = (f"{day:02}")
                        print(f"{year}-{month}-{day}")
                        break

            # September 12, 2005 format
            else:
                if "," not in in_date:
                    continue
                else:
                    month, day, year = in_date.split(" ")
                    if month.isdigit():
                        continue
                    else:
                        month = month.title()
                        day = day.strip(",")
                        day = int(day)

                        if month not in m:
                            continue
                        elif day > 31:
                            continue
                        else:
                            month = m.index(month) + 1
                            if day < 10:
                                day = (f"{day:02}")
                            if month < 10:
                                month = (f"{month:02}")
                            print(f"{year}-{month}-{day}")
                            break


        except EOFError:
            print("")
            break


main()
