age = int(input())

if age >= 18:
    print("You can drink")
else:
    print("No you can't")

n = int(input("Enter a value : "))

if(n < 0) :
    print("Negative")
elif (n == 0):
    print("Zero")
else:
    print("Positive")

# Switch case

match age:
    case 0:
        print("It is 0")
    case _ if age > 18:
        print("Valid")
    case _:
        print("invalid")
