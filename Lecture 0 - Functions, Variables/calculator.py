"""
x = int(input("What is x? "))
y = int(input("What is y? "))


z = int(x) + int(y)

print(x + y)
print(int(x) + int(y))
print(z)

#----------------------

print(int(input("What is x? ")) + int(input("What is Y? ")))

#----------------------

x = float(input("What is x? "))
y = float(input("What is y? "))

print(x + y)


#----------------------

x = float(input("What is x? "))
y = float(input("What is y? "))

z = round(x + y)

print(f"{z:,}")



#----------------------

x = float(input("What is x? "))
y = float(input("What is y? "))

z = (x / y)

print(z)

#----------------------

x = float(input("What is x? "))
y = float(input("What is y? "))

z = round(x / y, 2)



#----------------------
x = float(input("What is x? "))
y = float(input("What is y? "))

n = x / y
z = x / y

print(n)
print(f"{z:.2f}")

"""

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n
    #return n ** 2
    #return pow(n, 3)
    

main()


