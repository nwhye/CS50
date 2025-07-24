def main():
    expression = input("Expression: ")
    x, y, z, = expression.split(" ")

    first = float(x)
    second = float(z)

    if (y=="+"):
        answer = first + second
    elif (y=="-"):
        answer = first - second
    elif (y=="*"):
        answer = first * second
    elif (y=="/"):
        answer = first / second
    else:
        answer = None

    print(answer)

main()
