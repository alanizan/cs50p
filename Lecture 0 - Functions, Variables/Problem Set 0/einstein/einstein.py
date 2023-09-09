
def calc():
    #speed of light (measured approximately as 300000000 meters per second)
    c = 300000000
    #input mass entry as int
    m = int(input("m: "))
    # calculate mass by squared speed of light.
    e = m * pow(c, 2)
    print(e)

calc()
