from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()
f = ["-f", "--font"]


# when if elif done, move them to the end, and new if for checking wrong inputes

if len(sys.argv) == 1:
    x = input("Input: ")
    figlet.setFont(font=(random.choice(fonts)))  # "fonts" from list above
    print(figlet.renderText(x))


elif len(sys.argv) == 2:
    sys.exit("Invalid usage")


elif len(sys.argv) == 3:
    if sys.argv[1] not in f:
        sys.exit("Invalid usage")
    elif sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    else:
        x = input("Input: ")
        figlet.setFont(font=(sys.argv[2]))
        print(figlet.renderText(x))

