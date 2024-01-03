
answer = 0
column = 8

while column >= 1:
    bit = int(input("Enter bit value : "))
    answer = answer + column * bit
    column = column // 2
  
print("decimal value is :",answer)
