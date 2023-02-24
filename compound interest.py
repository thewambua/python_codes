principle=float(input("enter the priciple"))
rate=float(input("enter the rate"))
time=float(input("enter the time"))
amount=principle*(pow((1+rate/100),time))
ci=amount-principle
print("compound interest=",ci)
