from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = 'username', 'password', 'email', 'last_name', 'first_name', 'profession', 'fonction', 'photo', 'nom_prenoms'


class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()