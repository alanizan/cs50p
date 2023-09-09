"""
# Ask user for their name, remove spaces at the beginning, at the end (not the center) and capitalize names and returned a version of the word inserted titlecased
name = input ("What is your name? ").strip().title()

# Split user's name into first name and last name

first, last = name.split(" ")


# Remove whitespace from str

name = name.strip()

# Capitalize user name

name = name.capitalize()
name = name.title()

name = name.strip().title()



# Say hello to $name

print  ("hello, " + name)
print  ("hello,", name)
print(f"hello, {name}")
print(f"hello, {first, last}")




# print(*objects, sep=' ', end='\n', file=None, flush=False) example: https://docs.python.org/3/library/functions.html?highlight=print#print
print  ("Hello ",name, sep="???" )
print  ("Hello ", name, end="???")


def hello(to):
    print("hello,", to)

name = input ("What is your name? ")
hello(name)

"""

def main():
    name = input ("What is your name? ")
    salut(name)

def salut(to="empty"):
    print("hello,", to)




main()