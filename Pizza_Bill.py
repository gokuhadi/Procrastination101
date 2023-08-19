
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0 

if size == "s":
  bill +=15

elif size == "m":
  bill += 20
  
else:
  bill += 25


if add_pepperoni=="y":
  if size=="s":
      bill +=2
  else:
      bill +=3
if extra_cheese=="y":
  bill +=1

  
print (f"Total Bill is {bill}")
  
