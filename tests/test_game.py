from longest_word.game import Game


class TestGame:
    def test_game_initialization(self):

        game = Game()
        grid = game.grid

        assert len(grid) == 9
        assert type(grid) == list

    def test_is_valid(self):

        game = Game()
        game.grid = ['V', 'I', 'F', 'J', 'L', 'G', 'Z', 'E', 'A']
        word = 'AGILE'
        fake_word = 'EZUOBJ'

        assert game.is_valid(word=word) is True
        assert game.is_valid(word=fake_word) is False

    def test_is_a_word(self):

        game = Game()
        word = "VOLLEYBALL"
        fake_word = "NOTVOLLEYBALL"

        assert game.is_a_word(word=word) is True
        assert game.is_a_word(word=fake_word) is False
