# Demonstrates str functions

name = input("What's your name? ").strip().title().format(...)
first, last = name.split(" ")
print(f"hello, {first}")
