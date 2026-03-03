

name = input("Enter name: ")
age = int(input("Enter age: ")) #ypecast ie laver string om til int


age = age + 1

print(f"Hello {name} you are {age} +1 years old")

if age >= 18:
    print("you are welcome")
elif age == 17:
    print("youre still a kid habyibi")

elif age <= 17:
    print("cute")

name2 = ""
while name2 == "":
    print("you didnt type a name")
    name2 = input("enter name: ")
    