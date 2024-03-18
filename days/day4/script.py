lines = open("data.txt", "r").read().splitlines()


def part_one():
    total_points = 0

    for line in lines:
        winning_numbers = line.split(" | ")[0].split(": ")[-1].split(" ")
        winning_numbers = [int(x.strip(" ")) for x in winning_numbers if x != ""]

        my_numbers = line.split(" | ")[1].split(" ")
        my_numbers = [int(x.strip(" ")) for x in my_numbers if x != ""]

        points = 0
        for number in my_numbers:
            if number in winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2

        total_points += points

    print(f"Total points: {total_points}")



class Card:
    def __init__(self, string):
        self.card_number = None
        self.winning_numbers = None
        self.my_numbers = None

        self.from_string(string)

    def from_string(self, string):
        self.card_number = int(string.split(":")[0][5:])

        winning_numbers = string.split(" | ")[0].split(": ")[-1].split(" ")
        self.winning_numbers = [int(x.strip(" ")) for x in winning_numbers if x != ""]

        my_numbers = string.split(" | ")[1].split(" ")
        self.my_numbers = [int(x.strip(" ")) for x in my_numbers if x != ""]

    def get_n_matching(self):
        return len([x for x in self.my_numbers if x in self.winning_numbers])


def part_two():
    cards = [Card(line) for line in lines]
    total_cards = len(cards)

    card_winnings = {}

    for card in reversed(cards):
        n_matching = card.get_n_matching()
        new_cards = cards[card.card_number:card.card_number + n_matching]

        n_new_cards = len(new_cards)
        for new_card in new_cards:
            if new_card.card_number in card_winnings:
                n_new_cards += card_winnings[new_card.card_number]

        card_winnings[card.card_number] = n_new_cards
        total_cards += n_new_cards

    print("Total cards:", total_cards)




if __name__ == "__main__":
    part_two()