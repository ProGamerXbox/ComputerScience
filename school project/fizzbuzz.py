
HowFar = int(input("How far to count ? : "))

while HowFar < 1 :
    HowFar = int(input("not a valid number, please try again : "))
#endwhile

for MyLoop in range(1, HowFar + 1):
    if MyLoop % 3 == 0 and MyLoop % 5 == 0:
        print("FizzBuzz")
    elif MyLoop % 3 == 0:
        print("Fizz")
    elif MyLoop % 5 == 0:
        print("Buzz")
    else:
        print(MyLoop)
        #endif
    #endif
#endif
#endfor
