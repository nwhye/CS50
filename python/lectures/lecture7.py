# --- REGULAR EXPRESSIONS (regexes)
# define patterns in our code and compare them
# clean data

# --- email validation without regex
email = input("Enter your email: ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):  # "if username" is a valid syntax, as we ask true or false, exist or not
    print("Valid")
else:
    print("Invalid")

# we write a lot of code, and it's still not working properly


# --- RE.SEARCH

# re.search(pattern, string, flags=0)  # flag is to modify the behavior of the func
# if re.search("@", email)

'''
.  any character except a newline
*  0 or more repetitions
+  1 or more repetitions
?  0 or 1 repetitions
{m}  m repetitions (specific number of characters) 
{m,n}  m-n repetitions

^  matches the strat of the string
$  matches the end of the string or just before the newline at the end of the string

[]  set of characters that are allowed (or just one)
[^]  complementing the set (so you CAN NOT match any of this characters, but can ALL other symbols)

\w  word character - alphanumeric characters and underscore [a-zA-Z0-9_]
\W  not a word character
\d decimal digit [0-9]
\D  not a decimal digit
\s  whitespace characters
\S  not a whitespace character

A|B  either A or B
(...) a group to combine things (ALSO captures as a return value)
(?:...) non-capturing version
'''
# ..* is equal to .+
# [a-z] or [a-z ] to allow whitespace
# (com|edu|gov|net|org)  OR
# (\w|\s) - word or whitespaces
# (\w|\.) is equal to [a-z0-9_\.] (if used re.IGNORECASE)
import re

email = input("Enter your email: ").strip()

if re.search(r"^(\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    # .+ some character and more than one repetition. \ is to make . just a .
    # also IMPORTANT to put r - raw string, so it will treat \ as \n
    # ^ this pattern should match the start of the string, and $ this the end
    # [^] every symbol except @, so no repeating
    # (\w+\.)?  ? make it optional to add another domain once or 0 times
    # \.  escaped dot. using it just like a dot
    # (\w|\.) word OR just a dot

    # we can not only strip, but also lower(), but we can use flags - 3rd argument
    '''
    re.IGNORECASE
    re.MULTILINE  
    re.DOTALL   "." recognize any character + newline, not just any character
    '''
    # we can use f string, to pass the value of the variable into the pattern
    print("Valid")
else:
    print("Invalid")

    # re.search(r".+@.+" , email)
    # re.search(r".+@.+\.edu" , email)
    # re.search(r"^.+@.+\.edu&" , email)
    # re.search(r"^[^@]+@[^@]+\.edu$" , email)
    # re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email)
    # re.search(r"^\w+@\w+\.edu$", email)
    # re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE)
    # re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):


# --- RE.MATCH
# will automatically start matching from the start of the string. So no need to put ^

# --- RE.FULLMATCH
# will match start and the end of the string ( no ^ and $)

# --- CLEANING USER INPUT

name = input("Enter your name: ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{last}, {first}"
print(f"Hello, {name}")

# lets make stable version
# using GROUPS

import re

name = input("Enter your name: ").strip()
matches = re.search(r"^(.+), *(.+)$", name)  # (.+) in braces as we CAPTURE it
# * to tolerate whitespace or its absence
if matches:
    last, first = matches.groups()  # groups function is to ask what was captured (in our case in matches)
    name = f"{first}, {last}"
print(f"Hello, {name}")

# example how to take grom this group specific thing

name = input("Enter your name: ").strip()
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first}, {last}"
print(f"Hello, {name}")

# lets make tight version

name = input("Enter your name: ").strip()
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")

# --- WALRUS

name = input("Enter your name: ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):  # := is to assign AND ask boolean question (walrus)
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")

# --- EXTRACTING FROM STRING

url = input("Enter your url: ").strip()
username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")

# or

url = input("Enter your url: ").strip()
username = url.removeprefix("https://twitter.com/")  # it will not delete this if there is something in the beginning
print(f"Username: {username}")

# let's make it not fragile
# --- RE.SUB
# re.sub(pattern, repl, string, count=0, flags=0) - substitute(replace)
# useful for cleaning up data
import re

url = input("Enter your url: ").strip()
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)  # we must escape dot in the url
# ? to accept http and https (s?)
# (www\.)?  ? after so it can be there or not be there
# (https?://)? so if the user did not include protocol

print(f"Username: {username}")

# let's make it more conditional, so the user cannot write google or something else

import re

url = input("Enter your url: ").strip()
if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
# (.+) at the end to tolerate anything in the end AND CAPTURE IT
    print(f"Username: ", matches.group(3))

# let's clean it, so it will not capture (https?://) and (www\.)
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username: ", matches.group(1))

# (?:https?://) and (?:www\.)   ?: so only group, no capture

# also we can make it as
# (r"^(https?://)?(www\.)?twitter\.(?:com|org)/(.+)$")  OR
if matches := re.search(r"^(https?://)?(www\.)?twitter\.(.+)/(.+)$", url, re.IGNORECASE):
    if matches.group(1) == "com":
        print(f"Username: ", matches.group(2))


# --- FINAL VERSION

# r"^(https?://)?(www\.)?twitter\.com/(a-z0-9_)+)"

# without $, so anything can be printed after username, it still captures
# (a-z0-9_)+ as only this allowed to be in url of twitter
# (a-z0-9_)+  + as we tolerate one or more symbols


# --- RE.SPLIT
# split a string, using pattern

# --- RE.FINDALL
# allow to search multiple copies in one string
