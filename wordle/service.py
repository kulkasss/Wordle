import random

from .models import Game, Try
from django.conf import settings

class GameService:
    @staticmethod

    def random_word():
        with open(f"{settings.BASE_DIR}/filtered_ukr_nouns.txt", "r", encoding='utf-8') as file:
            read_content = file.read()
            return random.choice(read_content)
    @staticmethod
    def evaluate_guess(word, guess):
        green = 0
        for i in range(5):
            if word[i] == guess[i]:
                green += 1
        yellow = len(set(word) & set(guess)) - green
        return green, yellow

    @staticmethod
    def create_game(user):
        word = GameService.random_word()
        return Game.objects.create(user=user, word=word)

    @staticmethod
    def make_try(game, guess):
        green, yellow = GameService.evaluate_guess(game.word, guess)
        return Try.objects.create(game=game, guess=guess, green=green, yellow=yellow)
