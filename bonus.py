#enter salary and year of service
salary=int(input("enter salary amount"))
years_of_service=int(input("enter your years of service"))
if (years_of_service>10):
    bonus=0.1*salary
    print("your bonus is:",bonus )
elif(years_of_service >=6 and years_of_service <=10):
    bonus=0.08*salary
    print("your bonus is:",bonus)
elif(years_of_service <6):
    bonus=0.05*salary
    print("your bonus is:", bonus)
else:
    print("you have no bonus:")
    
