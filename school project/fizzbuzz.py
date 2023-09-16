
HowFar = int(input("How far to count ?"))

while int(HowFar) < 1 :
    HowFar = int(input("not a valid number, please try again"))
#endwhile

for MyLoop in [1, HowFar + 1]:
    if MyLoop % 3 == 0 and MyLoop % 5 == 0:
        print("FizzBuzz")
    else:
        if MyLoop % 3 == 0:
            print("Fizz")
        if MyLoop % 5 == 0:
            print("Buzz")
        else:
            print(MyLoop)
        #endif
    #endif
#endif
#endfor


