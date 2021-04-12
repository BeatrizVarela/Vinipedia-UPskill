from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from .models import Profile


# Formulário para o login
class LoginForm(forms.Form):
    username = forms.CharField(label="Username",
                               max_length=30,
                               widget=forms.TextInput(
                                   attrs={"class": "form-input",
                                          "placeholder": "Username"}))

    password = forms.CharField(label="Password",
                               max_length=30,
                               widget=forms.PasswordInput(
                                   attrs={"class": "form-input",
                                          "placeholder": "Password"}))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(
                                   attrs={"class": "form-input",
                                          "placeholder": "Password"}))

    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput(
                                    attrs={"class": "form-input",
                                           "placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Winetester99',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'John',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'cmon@hotgmail.com',
            })}

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


# TODO: Testar
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', )
