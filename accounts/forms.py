from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EditUserForm(forms.Form):

    newpassword1 = forms.CharField(max_length = 32, widget=forms.TextInput(attrs={'type':'password', 'placeholder':'New Password',  'class' : 'form-control'}))
    newpassword2 = forms.CharField(max_length = 32, widget=forms.TextInput(attrs={'type':'password', 'placeholder':'Confirm New Password',  'class' : 'form-control'}))


    def clean(self):
        if 'newpassword1' in self.cleaned_data and 'newpassword2' in self.cleaned_data:
            if self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
                raise forms.ValidationError("The two password fields did not match.")
        return self.cleaned_data