r=int(input("enter radius"))
h=int(input("enter height"))
pi=3.142
area=r*r*pi
def volume_of_a_cylinder(area,h):
    volume=area*h
    return volume
print(volume_of_a_cylinder(area,h))