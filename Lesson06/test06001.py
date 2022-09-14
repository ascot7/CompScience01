print("Welcome to macOS Terminal!")
print("Please refer to the user handbook for help.")
print(" ")
print(" ")


user = str(input("localhost login: "))
if user ==apple:
  print("user found")
  print(" ")
else:
  print("this user does not exist.")

pw = str(input("enter the pass for @apple: "))
if pw ==alpine:
  print("login accepted!")
  print("zsh> ")
else:
  print("incorrect password.")