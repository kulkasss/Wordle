import random

from .models import Game, Try
from django.conf import settings

class GameService:
    @staticmethod

    def random_word():
        with open(f"{settings.BASE_DIR}/filtered_ukr_nouns.txt", "r") as file:
            read_content = file.read()
            return random.choice(read_content)
    @staticmethod
    def evaluate_guess(letter, guess):
        word_str = str(letter)
        guess_str = str(guess)

        green = 0
        for i in range(5):
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
