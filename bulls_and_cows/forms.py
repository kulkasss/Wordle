from django import forms

from bulls_and_cows.models import Try


class TryForm(forms.ModelForm):
    class Meta:
        model = Try
        fields = ["guess"]
        labels = {"guess": "Ваш хід"}
        widget = {
            "guess": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Введіть 4-значне число"}
            )
        }
