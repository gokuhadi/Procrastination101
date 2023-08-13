print ("Welcome to  the rollercoaster!!\n")

height=int(input("What is your Height? "))

if height >= 120:
    print ("You can ride! Do not puke.")
    age=int(input("Enter your age- "))
    if age>18:
        print("Pay 12 Dollars")
    elif age<12 :
        print("Pay 5 Dollars")
    else:
        print("Pay 7 dollars")
else :
    print ("No rides for you! Sorry short kings..")
