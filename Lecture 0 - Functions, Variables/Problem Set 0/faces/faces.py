def main():
    e = input()
    print(convert(e))

def convert(emoji):
    return emoji.replace(":)", "🙂").replace(":(", "🙁")

main()