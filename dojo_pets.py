class Ninja:

    def __init__(self, first_name, last_name, pet, treats, pet_food) -> None:
        self.name = first_name + last_name
        # self.pet = pet
        self.pet_treats = treats
        self.pet_food = pet_food
        self.pet = Pet(name="", type="", tricks="", health="", energy="")

    def walk(self):
        pass

    def feed(self):
        pass

    def bathe(self):
        pass

class Pet:

    def __init__(self, name, type, tricks, health, energy) -> None:
        self.pet_name = name
        self.pet_type = type
        self.trick_type = tricks
        self.pet_health = health
        self.pet_energy = energy

    def sleep(self):
        pass

    def eat(self):
        pass

    def play(self):
        pass

    def noise(self):
        pass


splinter = Ninja("Master ", "Splinter", "carrots", "pizza")
donatello = Pet("Donatello", "turtle", "Bo Staff", "super", "ninja")


splinter.pet.pet_name = "Donatello"
print(splinter.pet.pet_name)

splinter.pet = Pet("Donatello", "turtle", "Bo Staff", "super", "ninja")

print(splinter.pet.pet_name)