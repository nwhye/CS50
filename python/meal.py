def main():
    time = input("What time is it? ")
    answer = convert(time)

    if(7<=answer<=8):
        print("breakfast time")
    elif(12<=answer<=13):
        print("lunch time")
    elif(18<=answer<=19):
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes)
    hours = float(hours)
    m = minutes / 60
    result = hours + m
    return(result)

if __name__ == "__main__":
    main()
