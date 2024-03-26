def greet(name):
    if name == "Surbhi":
        return "Ma'am"
    else:
        return "sir"


name=str(input("Please Enter your name: "))
print("Hello",greet(name))
