print("\nHello!")
userNum = int(input("""Please enter a number and I will tell you if your number
is odd or even > """))

def isOddOrEven(num):
    if num % 2 == 0:
        print("\nYou entered an even number!")
    elif num % 2 == 1:
        print("\nYou entered an odd number!")

isOddOrEven(userNum)
