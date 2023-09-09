def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d =  float(d.replace("$",""))
    return (d)


def percent_to_float(p):
    if p != "15%":
        print("wrong entry, insert 15%")
    else:
        p =  float(p.replace("%",""))/(100)
        return (p)
main()