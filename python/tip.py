def main():
    dollars = dollars_to_float(input("How much was the meal? ").strip('$'))
    percent = persent_to_float(input("What percent to you want to tip? ").strip('%'))
    tip = dollars * percent
    print(f"Leave: ${tip:.2f}")

def dollars_to_float(d):
    meow = float(d)
    return meow

def persent_to_float(p):
    pp = float(p)*0.01
    return pp

main()
