class Ninja:

    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.name = first_name + last_name
        self.pet = pet
        self.pet_treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

class Pet:

    def __init__(self, name, type, tricks):
        self.pet_name = name
        self.pet_type = type
        self.trick_type = tricks
        self.pet_health = 0
        self.pet_energy = 0

    def sleep(self):
        self.pet_energy += 25
        return self

    def eat(self):
        self.pet_energy += 5
        self.pet_health += 10
        return self

    def play(self):
        self.pet_health += 5
        return self

    def noise(self):
        print(f"your {self.pet_type} made whatever noise a {self.pet_type} makes.")
        return self


donatello = Pet("Donatello", "turtle", "Bo Staff",)
splinter = Ninja("Master ", "Splinter", donatello, "carrots", "pizza")


splinter.feed().walk().bathe()
print(donatello.pet_health)
print(donatello.pet_energy)

