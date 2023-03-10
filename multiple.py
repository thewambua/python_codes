#python program to implement multiple inheritance 
class Animal:
    def legs(self):
        print("I have four legs")
    def fur(self):
        print("My body is covered with fur")
class Dog:
    def bark(self):
        print("The dog barks")
class Domestic(Animal,Dog):
    def live(self):
        print("Domestic animal lives at home")
d = Domestic()
d.bark()
d.live()
d.legs()
d.fur()