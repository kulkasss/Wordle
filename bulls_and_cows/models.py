from django.contrib import admin
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Game(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="games", verbose_name="Користувач"
    )
    number = models.PositiveIntegerField(
        "Загадане слово", validators=[MinValueValidator(1000), MaxValueValidator(9999)]
    )
    created_at = models.DateTimeField("Дата створення", auto_now_add=True)

    class Meta:
        verbose_name = "Гра"
        verbose_name_plural = "Гри"

    def __str__(self):
        return f"Game #{self.pk} for {self.user.username}"

    @property
    @admin.display(boolean=True, description='Завершено')
    def is_finished(self):
        return self.tries.filter(bulls=4).exists()

    @property
    @admin.display(description='Кількість спроб')
    def tries_count(self):
        return self.tries.count()


class Try(models.Model):
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name="tries", verbose_name="Гра"
    )
    guess = models.PositiveIntegerField(
        "Хід", validators=[MinValueValidator(1000), MaxValueValidator(9999)]
    )
    bulls = models.PositiveIntegerField("Бики")
    cows = models.PositiveIntegerField("Корови")
    created_at = models.DateTimeField("Дата спроби", auto_now_add=True)

    class Meta:
        verbose_name = "Спроба"
        verbose_name_plural = "Спроби"

    def __str__(self):
        return f"Try {self.guess}"
