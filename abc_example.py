from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, number_of_legs):
        self.name=name
        self.number_of_legs = number_of_legs
    
    @abstractmethod
    def eat(self):
        pass
    
    def walk(self):
        print("I will walk 500 hundred miles")

class Dog(Animal):
    def __init__(self, name, favorite_snack):
        super().__init__(name, 4)

        self.favorite_snack = favorite_snack

    def eat(self):
        print("Om nom nom")

class Cat(Animal):
    def __init__(self, name, is_annoying):
        super().__init__(name, 4)

        self.is_annoying = is_annoying
    
    def eat(self):
        print("Chop chop chop")

class Giraffe(Animal):
    def __init__(self, name):
        super().__init__(name, 4)

    def eat(self):
        print("Yum yum")

    def walk(self):
        super().walk()
        print("The giraffe is walking")

if __name__ == "__main__":
    animal = Giraffe("Jira")


    animal.eat()
    animal.walk()
    print(animal.name)