from string import ascii_letters
import random
import requests as rq


class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = [random.choice(ascii_letters).upper() for i in range(9)]

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        word_in_grid = all([letter in self.grid for letter in word])
        return word_in_grid and self.is_a_word(word=word)

    def is_a_word(self, word: str) -> bool:
        """Return True if and only if the word is in the English dictionary"""
        dictionary_url = "https://api.dictionaryapi.dev/api/v2/entries/en"
        return rq.get(f"{dictionary_url}/{word}", timeout=10).status_code == 200
