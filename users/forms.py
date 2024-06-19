from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Name"}))
    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Password"}))


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Username"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Phone Number"}))
    first_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Last Name"}))
    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Confirm Password"}))
    user_role = forms.Select(attrs={'class': "form-control"})

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'first_name', 'last_name', 'password', 'confirm_password', 'user_role')


class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Last Name"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Phone Number"}))
    email = forms.CharField(widget=forms.TextInput({"class":"form-control", "placeholder": "Email"}))
    address = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Address"}))
    image = forms.ImageField(widget=forms.FileInput({"class": "form-control", "placeholder": "Image"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address', 'image']


class ClientRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput({'class': 'form-control'}), required=True)
    phone_number = forms.CharField(widget=forms.TextInput({'class': 'form-control'}), required=False)
    password1 = forms.CharField(widget=forms.PasswordInput({'class': 'form-control'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput({'class': 'form-control'}), required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'phone_number')

    def save(self, commit=True):
        user = super(ClientRegistrationForm, self).save(commit=False)
        user.user_role = 'client'
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user


