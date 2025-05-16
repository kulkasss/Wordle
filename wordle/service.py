import random

from .models import Game, Try


class GameService:
    @staticmethod
    def generate_word():
        digits = random.sample(range(10), 4)
        if digits[0] == 0:
            digits[0], digits[1] = digits[1], digits[0]
        return int("".join(map(str, digits)))

    @staticmethod
    def evaluate_guess(letter, guess):
        word_str = str(letter)
        guess_str = str(guess)

        green = 0
        for i in range(4):
            if word_str[i] == guess_str[i]:
                green += 1

        yellow = len(set(word_str) & set(guess_str)) - green

        return green, yellow

    @staticmethod
    def create_game(user):
        word = GameService.generate_word()
        return Game.objects.create(user=user, word=word)

    @staticmethod
    def make_try(game, guess):
        green, yellow = GameService.evaluate_guess(game.letter, guess)
        return Try.objects.create(game=game, guess=guess, green=green, yellow=yellow)
