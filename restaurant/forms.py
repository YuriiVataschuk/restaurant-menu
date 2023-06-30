from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from restaurant.models import Dish, Cook


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )

    def clean_license_number(self) -> str:
        return validate_years_of_experience(
            self.cleaned_data["years_of_experience"]
        )


class CookExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["years_of_experience"]

    def clean_license_number(self) -> str:
        return validate_years_of_experience(
            self.cleaned_data["years_of_experience"]
        )


def validate_years_of_experience(
        years_of_experience,
) -> str:  # regex validation is also possible here
    if years_of_experience < 1:
        raise ValidationError(
            "Our restaurant does not hire cooks "
            "without at least 1 year of experience"
        )
    elif years_of_experience >= 60:
        raise ValidationError("It is impossible to have such experience")

    return years_of_experience


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username"}
        )

    )


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )
