from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput, Select

from userextend.models import UserExtend


class UserExtendForm(UserCreationForm):
    class Meta:
        model = UserExtend
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'city', 'gender', 'address']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Please enter your username', 'class': 'form-control'}),
            'email': EmailInput(attrs={'required': 'true', 'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'phone': TextInput(attrs={'placeholder': 'Please enter your phone number', 'class': 'form-control'}),
            'city': TextInput(attrs={'placeholder': 'Please enter your city', 'class': 'form-control'}),
            'gender': Select(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'placeholder': 'Please enter you address', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
