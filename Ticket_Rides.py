print ("Welcome to  the rollercoaster!!\n")

height=int(input("What is your Height? "))
bill=0

if height >= 120:
    print ("You can ride! Do not puke.")
    age=int(input("Enter your age- "))
    if age>18 and age<=45:
        bill=12
        print("Pay 12 Dollars")
    elif age >45 and age<55:
        bill=0
        print ("pay 0 for the tickets")
    elif age<12:
        bill=5
        print("Pay 5 Dollars")
    else:
        bill=7
        print("Pay 7 dollars")
    wants_photo = input("Do you want a photo? Y or N ")
    if wants_photo == "y":
        bill+=3
        print(f"Total is {bill}")
    else:
        print(f"Total bill without the pic is {bill}")
else :
    print ("No rides for you! Sorry short kings..")
  
