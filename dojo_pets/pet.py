
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


class Reptile(Pet):

    def __init__(self, name, type, tricks, enemy):
        super().__inti__(name, type, tricks)
        self.enemy = enemy


