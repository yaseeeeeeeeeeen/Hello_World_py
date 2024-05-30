#User Input.

name =input("enter your name : ")
age=int(input("enter your age :"))
age=age+1
location=input("where are you from ? :")

print(f"Welcome to our community! Meet {name}, a {age}-year-old from the beautiful place of {location}.")


length=float(input("Enter the lenghth :"))
width=float(input("enter the width :"))
area=length*width
print(f"Area is {area}")


item=input("What item you like to buy?")
quatity=int(input("how much you buy?"))
price=float(input("How much the price for one piece?"))

print(f"your purchased {quatity} {item}s")
total=quatity*price
print(f"total ammount is {quatity} x {price} : {total}")