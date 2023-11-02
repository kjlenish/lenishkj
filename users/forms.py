from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,
                                help_text="Enter your first name.", label='First Name')
    last_name = forms.CharField(max_length=30, required=True, 
                                help_text="Enter your last name.", label='Last Name')
    email = forms.EmailField(max_length=254, required=True, 
                             help_text="Enter a valid email address.", label='Email')
    password2 = forms.CharField(widget=forms.PasswordInput, 
                            help_text="Renter the password.", label='Confirm Password')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


# class ProfileSignUpForm(forms.ModelForm):
#     user = forms.OneToOneField(User,null=True, on_delete=models.CASCADE)
#     profile_img = forms.ImageField(default='profile_picture\default.jpg', upload_to='profile_picture')
#     country_code = forms.CharField(max_length=5, default=None, blank=True, null=True)
#     phone = forms.CharField(max_length=15, default=None, blank=True, null=True)
#     dob = forms.DateField(default=None, blank=True, null=True)
#     fav_mov = forms.TextField(default=None, blank=True, null=True)
#     date_created = forms.DateField(auto_now_add=True, null=True)

#     class Meta:
#         model = Profile
#         fields = ['profile_img', 'country_code', 'phone', 'dob', 'fav_mov']



class LoginForm(forms.Form):
   username = forms.CharField()
   password = forms.CharField(widget=forms.PasswordInput)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_img', 'country_code', 'phone', 'dob', 'fav_mov']

