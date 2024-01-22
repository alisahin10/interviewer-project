from django import forms
from django.contrib.auth.models import User
from account.models import Profile
from interviewer.models import Contact

"""
class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)


        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. 
            Letters, digits and @/./+/-/_ only.</small></span>'


class UserPictureForm(forms.ModelForm):
    image = forms.ImageField(label="Profile Picture", required=False)  # Add the ImageField for the 'image' field

    class Meta:

        model = Profile
        fields = ('image',)

    def __init__(self, *args, **kwargs):
        super(UserPictureForm, self).__init__(*args, **kwargs)
"""

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

