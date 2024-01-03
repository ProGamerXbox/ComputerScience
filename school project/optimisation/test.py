
def even(x):
    if x % 2 != 0:
        return False
    else:
        return True
    
# steps 1

def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

# step 2


def even(x):
    if x % 2 == 0:
        return True
    return False

# step 3

def even(x):
    return x % 2 == 0

def odd(x):
    return not even(x)

# 2nd

x = 1.0

while x != x + 1.0:
    x *= 2.0

print('END')

# 3rd

nums = [2,1,4]
text = "COMPUTERS"

nums.sort(reverse=True)

for index in nums:
    text = text[:index] + text[(index + 1):]
print(text)