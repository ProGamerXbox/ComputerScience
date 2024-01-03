
hangman_list = open('wordlist.txt').read()
alphabet = open('alphabet.txt').read().split()

a_count = 0
z_count = 0

for i in hangman_list:
   
    if i == alphabet[0]:
        a_count += 1
    if i == alphabet[-1]:
        z_count += 1
    #print(i)

print("There is", a_count, "'a' letters")
print("There is", z_count, "'z' letters")