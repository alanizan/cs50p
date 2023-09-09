hello = input("Greeting: ").strip().lower()
match hello:
    case "hello" | "h" | "hello, newman":
        print("$0")
    case "how you doing?" | "hey":
        print("$20")
    case _:
        print("$100")



