from django import forms

from wordle.models import Try


class TryForm(forms.ModelForm):
    class Meta:
        model = Try
        fields = ["guess"]
        labels = {"guess": "Ваш хід"}
        widget = dict(guess=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введіть слово з 5 букв"}
        ))
