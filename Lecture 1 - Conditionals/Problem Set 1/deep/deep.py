a = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower().replace("-"," ")

if a == "42" or a == "forty two":
    print("Yes")
else:
    print("No")
