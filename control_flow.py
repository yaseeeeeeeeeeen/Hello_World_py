#IF ELSE ELIF

age = int(input("Enter your age :"))
if age >= 18:
    print("Now you can signup!")
elif age < 0:
    print("You haven't been born yet.!")

else:
    print(f"Must be 18+, your still {age}.")

# If using Bool
online = False
if online:
    print("this user is Online")
else:
    print("This user is offline")