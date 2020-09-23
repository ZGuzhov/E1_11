import pytest
import random
import gallows


words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
letters = 'abcefgiklnoprstuvxy'
secret = random.choice(words)


def test_game():
    result_game = gallows.game(words, True)
    if result_game == 'Вы выиграли! Поздравляю!' or result_game == 'Вы проиграли. Попытки закончились.':
        assert True
    else:
        assert False
