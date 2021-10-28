
import ninja
import pet

donatello = pet.Pet("Donatello", "turtle", "Bo Staff",)
splinter = ninja.Ninja("Master ", "Splinter", donatello, "carrots", "pizza")


splinter.feed().walk().bathe()
print(donatello.pet_health)
print(donatello.pet_energy)
print(donatello.pet_name)


snake = pet.Reptile("snake", "reptile", "slither", "owl")
snake.eat()
print(snake.pet_name)