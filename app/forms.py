from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Property, User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password','is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('email',)

class SearchDetailForm(forms.Form):
    acccess_distance = forms.IntegerField(
        label='acccess_distance',
        widget=forms.NumberInput,
        required=False,)
    age = forms.IntegerField(
        label='age',
        widget=forms.NumberInput,
        required=False,)
    menseki = forms.IntegerField(
        label='menseki',
        widget=forms.NumberInput,
        required=False,)
    price = forms.IntegerField(
        label='price',
        widget=forms.NumberInput,
        required=False,)
