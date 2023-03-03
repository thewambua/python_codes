#enter marks of subjects
Physics=int(input("enter marks for Physics"))
Computer=int(input("enter marks for Computer"))
Maths=int(input("enter marks for Maths"))
average=(Physics+Computer+Maths)/3
print("average is",average)
if (average>=70 and average <=100):
    print("Grade: A")
elif (average>=60 and average>=69):
    print("Grade: B")
elif (average>=50 and average  <=59):
    print("Grade: C")
elif (average>=40 and average <=49):
    print("Grade: D")
elif (average>=0 and average <=39):
    print("Grade: FAIL")
else:
    print("marks are not in the criteria")
    
