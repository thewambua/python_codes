#python program to implement hierachical inheritance
class Animal:
    def legs(self):
        print("I have four legs")
    def fur(self):
        print("My body is covered with fur")
class Dog(Animal):
    def bark(self):
        print("The dog barks")
class Carnivore(Animal):
    def meat(self):
        print("Carnivores eat meat")
c = Carnivore()
c.meat()
c.legs()
c.fur()



