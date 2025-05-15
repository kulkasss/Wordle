import random

from .models import Game, Try


class GameService:
    @staticmethod
    def generate_number():
        digits = random.sample(range(10), 4)
        if digits[0] == 0:
            digits[0], digits[1] = digits[1], digits[0]
        return int("".join(map(str, digits)))

    @staticmethod
    def evaluate_guess(number, guess):
        number_str = str(number)
        guess_str = str(guess)

        bulls = 0
        for i in range(4):
            if number_str[i] == guess_str[i]:
                bulls += 1

        cows = len(set(number_str) & set(guess_str)) - bulls

        return bulls, cows

    @staticmethod
    def create_game(user):
        number = GameService.generate_number()
        return Game.objects.create(user=user, number=number)

    @staticmethod
    def make_try(game, guess):
        bulls, cows = GameService.evaluate_guess(game.number, guess)
        return Try.objects.create(game=game, guess=guess, bulls=bulls, cows=cows)
