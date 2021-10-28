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
