from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

ARCANA = (
    ('The Fool', '0 The Fool'),
    ('The Magician', 'I The Magician'),
    ('The High Priestess', 'II The High Priestess'),
    ('The Empress', 'III The Empress'),
    ('The Emperor', 'IV The Emperor'),
    ('The Hierophant', 'V The Hierophant'),
    ('The Lovers', 'VI The Lovers'),
    ('The Chariot', 'VII The Chariot'),
    ('Justice', 'VIII Justice'),
    ('The Hermit', 'IX The Hermit'),
    ('Wheel of Fortune', 'X Wheel of Fortune'),
    ('Strength', 'XI Strength'),
    ('The Hanged Man', 'XII The Hanged Man'),
    ('Death', 'XIII Death'),
    ('Temperance', 'XIV Temperance'),
    ('The Devil', 'XV The Devil'),
    ('The Tower', 'XVI The Tower'),
    ('The Star', 'XVII The Star'),
    ('The Moon', 'XVIII The Moon'),
    ('The Sun', 'XIX The Sun'),
    ('Judgement', 'XX Judgement'),
)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    arcana = forms.CharField(label='Arcana', widget=forms.Select(choices=ARCANA))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    arcana = forms.CharField(label='Arcana', widget=forms.Select(choices=ARCANA))

    class Meta:
        model = Profile
        fields = ['image', 'arcana']    