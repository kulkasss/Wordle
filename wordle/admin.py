from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Game, Try


# Інлайн для відображення спроб гри
class TryInline(admin.TabularInline):
    model = Try
    extra = 0  # Не показувати порожні рядки


# Налаштування адміністрування для гри
class GameAdmin(admin.ModelAdmin):
    # Список стовпців, які відображаються на сторінці списку
    list_display = ("user", "number", "tries_count", "is_finished", "created_at")
    # Фільтри за користувачем і завершеністю гри
    list_filter = ("user",)
    # Поля для пошуку
    search_fields = ("user__username", "number")
    # Відображення спроб гри в адмінці
    inlines = [TryInline]
    # Ієрархія за датою
    date_hierarchy = "created_at"

    # Оптимізація запитів, щоб завантажувати спроби разом з грою
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related("tries")  # Завантажуємо спроби разом з грою


# Реєстрація моделі Game у адмінці
admin.site.register(Game, GameAdmin)

# Вилучаємо модель Group з адмінки
admin.site.unregister(Group)
