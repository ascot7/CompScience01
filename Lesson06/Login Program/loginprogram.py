print("Welcome to macOS Terminal!")
print("Please refer to the user handbook for help.")
print(" ")
print(" ")

loginUser = input("localhost login: ")
loginPass = input("localhost password: ")

if(loginUser == "apple"):
  if(loginPass == "alpine"):
    print("Login Success!")
    print("Welcome to the macOS Kernel")
    print(" ")
    print("zsh>")
  else:
    print("Invalid Password")
else:
  print("This user does not exist")