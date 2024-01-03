

def is_alphabetic(char):
    return 'A' <= char <= 'Z' or 'a' <= char <= 'z'

def encrypt(plaintext: str, key: int) -> str:

    plaintext = input("Enter your super secret message : ")
    plaintext = plaintext.upper()
    charactercode = list(map(ord, plaintext))

    while True:
        key = int(input("What key (number from 1 to 25)? : "))
        if key > 25 or key < 0:
            print("You must choose between 1 to 25 : ")
        else:
            break

    print("""
[*] Your super secure encrypted message with is :
##########################""")
    for char in plaintext:
        if is_alphabetic(char):
            charactercode = ord(char)
            charactercode = (charactercode - ord('A') - key) % 26 + ord('A')
            print(chr(charactercode), end='')
        else:
            print(char, end='')
    print("""
##########################""")

def decrypt(ciphertext: str, key: int) -> str:

    ciphertext = input("\nEnter the super secret message to decrypt : ")
    ciphertext = ciphertext.upper()

    while True:
        key = int(input("What key (number from 1 to 25)? : "))
        if key > 25 or key < 0:
            print("You must choose between 1 to 25 : ")
        else:
            break

    real_key = -key

    print("\nThe key you have chosen is : ", key)
    
    print("""
[*] The encrypted message is :
##########################""")
    for char in ciphertext:
        if is_alphabetic(char):
            charactercode = ord(char)
            charactercode = (charactercode - ord('A') - real_key) % 26 + ord('A')
            print(chr(charactercode), end='')
        else:
            print(char, end='')
    print("""
##########################""")

encrypt(1, 2)
decrypt(1, 2)