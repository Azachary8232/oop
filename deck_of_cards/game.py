from classes.deck import Deck
import random


# bicycle.show_cards()


class Game:
    bicycle = Deck()

    def __init__(self,name, game_type,):
        self.game_name = game_type
        self.new_list = []
        self.new_card = ""
        self.receive = ""
        self.name = name

    def get_card(self,):
        self.new_list = (self.bicycle.cards)
        self.new_card = self.new_list[random.randint(0, 51)]
        # self.new_card.card_info()
        self.receive = f"{self.name} gets " + self.new_card.card_info()
        print(self.receive)

class People(Game):
    
    def __init__(self, name):
        self.name = name

tom = Game("Tom", "Black Jack21")
dealer = Game("Dealer", "Black Jack21")
# black_jack = Game("Black Jack21")

# print(tom.name)
# print(black_jack.game_name)
# black_jack.get_card()

tom.get_card()
dealer.get_card()
tom.get_card()
dealer.get_card()
