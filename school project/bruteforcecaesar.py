
def is_alphabetic(char):
    return 'A' <= char <= 'Z' or 'a' <= char <= 'z'

def decrypt(ciphertext: str, key: int) -> str:
    crack = 1

    ciphertext = input("Enter the super secret message to brute force : ")
    ciphertext = ciphertext.upper()

    print("""
[*] Brute force of all keys :
##########################""")
    while crack < 26:
        for char in ciphertext:
            if is_alphabetic(char):
                charactercode = ord(char)
                charactercode = (charactercode - ord('A') - crack) % 26 + ord('A')
                print(chr(charactercode), end='')
            else:
                print(char, end='')
        print(" | key : ", crack)
        crack += 1
    print("""##########################""")
decrypt(1, 2)