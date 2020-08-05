"""Python implementation of a trading game based on Jaipur"""

import random

NUM_DIAMOND = 6
NUM_GOLD = 6
NUM_SILVER = 6
NUM_CLOTH = 8
NUM_SPICES = 8
NUM_LEATHER = 10
NUM_CAMEL = 8

INITIAL_HAND_LENGTH = 5

CARD_TYPES = {
    "Diamond": NUM_DIAMOND,
    "Gold": NUM_GOLD,
    "Silver": NUM_SILVER,
    "Cloth": NUM_CLOTH,
    "Spices": NUM_SPICES,
    "Leather": NUM_LEATHER,
    "Camel": NUM_CAMEL
}

CHIP_VALUES = {
    "Diamond": [5, 5, 5, 7, 7],
    "Gold": [5, 5, 5, 6, 6],
    "Silver": [5, 5, 5, 5, 5],
    "Cloth": [1, 1, 2, 2, 3, 3, 3],
    "Spices": [1, 1, 2, 2, 3, 3, 5],
    "Leather": [1, 1, 1, 1, 1, 1, 2, 3, 4]
}

BONUS_THREE = [1, 1, 2, 2, 2, 3, 3]
BONUS_FOUR = [4, 4, 5, 5, 6, 6]
BONUS_FIVE = [8, 8, 9, 10, 10]

class Card:
    """Representation of Playing Cards"""
    def __init__(self, card_type: str) -> None:
        self.card_type = card_type

    def __repr__(self) -> None:
        return f"{self.card_type}"

class Chip:
    """Representation of Playing Chips"""
    def __init__(self, chip_type: str, value: int) -> None:
        self.chip_type = chip_type
        self.value = value

class ChipStack():
    """Representation of a Stack of Available Chips"""
    def __init__(self, chip_type: str) -> None:
        self.chips = CHIP_VALUES[chip_type]

    def __repr__(self) -> str:
        return f"{self.chips}"

class ChipMarket():
    """Representation of all available chips"""
    def __init__(self) -> None:
        self.diamond = ChipStack("Diamond")
        self.gold = ChipStack("Gold")
        self.silver = ChipStack("Silver")
        self.cloth = ChipStack("Cloth")
        self.spices = ChipStack("Spices")
        self.leather = ChipStack("Leather")

    def __repr__(self) -> str:
        return f"""
        Diamond: {self.diamond}
        Gold: {self.gold}
        Silver: {self.silver}
        Cloth: {self.cloth}
        Spices: {self.spices} 
        Leather: {self.leather}"""

class Hand:
    """Player Hand"""
    def __init__(self) -> None:
        self.cards = []
        self.herd = []

    def has_three_of_a_good(self) -> bool:
        """Check if the hand has 3 of any type of good"""
        return self.__has_n_of_a_good(3)

    def has_four_of_a_good(self) -> bool:
        """Check if the hand has 4 of any type of good"""
        return self.__has_n_of_a_good(4)

    def has_five_of_a_good(self) -> bool:
        """Check if the hand has 5 of any type of good"""
        return self.__has_n_of_a_good(5)

    def has_good(self, good: str, n: int = 1) -> bool:
        """Check if the hand has some number n of a particular good"""
        assert n >= 1 & n <= 7

        count = 0
        for card in self.cards:
            if card.card_type == good:
                count += 1
        if count >= n:
            return True
        return False

    def summarize(self) -> dict:
        summary = {key:0 for key in CARD_TYPES}
        for card in self.cards:
            summary[card.card_type] += 1
        summary["Camel"] += len(self.herd)
        return summary

    def __has_n_of_a_good(self, n: int) -> bool:
        for good in CARD_TYPES:
            if good == "Camel":
                next
            if self.has_good(good, n):
                return True
        return False

    def __repr__(self) -> str:
        return f"""Goods: {self.cards}, Camels: {len(self.herd)}"""

class Deck:
    """Representation of Deck"""
    def __init__(self, shuffle: bool = True) -> None:
        self.cards = []
        for card_type in CARD_TYPES:
            for _ in range(CARD_TYPES[card_type]):
                self.cards.append(Card(card_type))
        if shuffle:
            self.shuffle()

    def shuffle(self) -> None:
        """Shuffles the deck"""
        length = len(self.cards)
        for i in range(length):
            selected = random.randint(i, length - 1)
            temp = self.cards[i]
            self.cards[i] = self.cards[selected]
            self.cards[selected] = temp

    def deal_hand(self, hand: Hand) -> None:
        """Deals cards from Deck to a specified hand object"""
        for _ in range(INITIAL_HAND_LENGTH):
            temp = self.cards.pop()
            if temp.card_type == "Camel":
                hand.herd.append(temp)
            else:
                hand.cards.append(temp)

class Market:
    """Representation of Market"""
    def __init__(self) -> None:
        self.cards = []

class Discard:
    """Representation of Discard Pile"""
    def __init__(self) -> None:
        self.cards = []