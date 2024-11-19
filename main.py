class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animals(self, animals):
        self.animals.extend(animals)

    def add_staff_members(self, staff_members):
        self.staff.extend(staff_members)

    def call_animals(self):
        for animal in self.animals:
            animal.make_sound()

    def assign_work(self, animal):
        for staff_member in self.staff:
            staff_member.work(animal)


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        pass


class ZooKeeper(Employee):
    def work(self, animal):
        print(f"{self.name} is taking care of {animal.name}.")


class Veterinarian(Employee):
    def work(self, animal):
        print(f"{self.name} is treating {animal.name}.")


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        return f"{self.name} is eating."


class Bird(Animal):
    def make_sound(self):
        print(f"A {__class__.__name__.lower()} named {self.name} chirps.")


class Mammal(Animal):
    def make_sound(self):
        print(f"A {__class__.__name__.lower()} named {self.name} growls.")


class Reptile(Animal):
    def make_sound(self):
        print(f"A {__class__.__name__.lower()} named {self.name} hisses.")


zoo = Zoo()

bird1 = Bird("Robin", 2)
bird2 = Bird("Sparrow", 1)
mammal1 = Mammal("Lion", 5)
reptile1 = Reptile("Snake", 3)

keeper1 = ZooKeeper("John", 30)
vet1 = Veterinarian("Dr. Smith", 45)

zoo.add_animals([bird1, bird2, mammal1, reptile1])
zoo.add_staff_members([keeper1, vet1])

zoo.call_animals()
zoo.assign_work(mammal1)
