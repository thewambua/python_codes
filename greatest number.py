#enter three numbers
x = int(input("No 1\n"))
y = int(input("No 2\n"))
z = int(input("No 3\n"))
if x>y and x>z:
    print("The greater number is",x)
elif y>x and y>z:
    print("The greater number is",y)
else:
    print("The greater number is",z)
    
