
def check():
    ask = input("[*] - Enter the string: ")
    unique = len(set(ask)) == len(ask)

    add_value = sum(ord(char) for char in ask)

    if 5 <= len(ask) <= 7 and ask.isupper() and 420 <= add_value <= 600 and unique:
        print("\n[!] - the string satisfies the conditions")
    else:
        print("[*] - Doesn't satisfies the conditions")
        check()
check()
