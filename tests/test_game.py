from longest_word.game import Game


class TestGame:
    def test_game_initialization(self):
        """A grid which size is 9 and is a list should be valid"""
        game = Game()
        grid = game.grid

        assert len(grid) == 9
        assert type(grid) == list

    def test_is_valid(self):
        """A word which letters are in the grid should be valid"""
        game = Game()
        game.grid = ['V', 'I', 'F', 'J', 'L', 'G', 'Z', 'E', 'A']
        word = 'AGILE'
        fake_word = 'EZUOBJ'

        assert game.is_valid(word=word) is True
        assert game.is_valid(word=fake_word) is False

    def test_is_a_word(self):
        """A word that exists in english directory should be valid"""
        game = Game()
        word = "VOLLEYBALL"
        fake_word = "NOTVOLLEYBALL"

        assert game.is_a_word(word=word) is True
        assert game.is_a_word(word=fake_word) is False

    def test_unknown_word_is_invalid(self):
        """A word that is not in the english directory should no be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
