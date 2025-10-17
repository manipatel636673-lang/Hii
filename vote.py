#vote.py
try:
  age=int(input("enter your age : "))
  if age >= 18:
    grint("your are eligible to vote")
  else:
    print("you are not eligible to vote")
except ValueError:
  print("please enter a valid integer")
  
