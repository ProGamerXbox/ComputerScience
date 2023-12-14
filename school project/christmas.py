
# "ABABBC" => "BABC"

# when we find repetitive letters, we want to delete duplicates
# list, map to pass in each letter - have I encouted the letter before ?

#key = 'A'
#textdict[key] = 100
text = input("Enter a string : ")
textdict = {}
indexes = {}

for index, letter in enumerate(text):
    print(index, letter)
    try:
        indexes[letter]
    except:
        indexes[letter] = []
    indexes[letter].append(index)

for key,value in indexes.items():
    value.pop()
    print(key,value)
    