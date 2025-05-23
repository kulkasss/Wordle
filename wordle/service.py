import random

from .models import Game, Try


class GameService:
    @staticmethod

    def generate_word_from_file(filtered_ukr_nouns.txt):
        with open(filtered_ukr_nouns.txt, 'r', encoding='utf-8') as file:
            words = [line.strip() for line in file if len(line.strip()) == 5]

        if not words:
            raise ValueError("У файлі немає слів з 5 літерами.")

        return random.choice(words)
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
