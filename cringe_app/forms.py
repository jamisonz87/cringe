from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Thread, Reply

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'username')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class':'input is-medium', 'placeholder': 'Enter Username'})
        self.fields['email'].widget.attrs.update({'class':'input is-medium', 'placeholder': 'Enter Email'})
        self.fields['password1'].widget.attrs.update({'class':'input is-medium', 'placeholder': 'Enter Password'})
        self.fields['password2'].widget.attrs.update({'class':'input is-medium', 'placeholder': 'Confirm Password'})

    def save(self, commit=True):
        user = super().save(commit=False)
        
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ExtendedAuthenicationForm(AuthenticationForm):
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({'class':'input is-medium', 'placeholder': 'Enter Username'})
            self.fields['password'].widget.attrs.update({'class':'input is-medium', 'placeholder': 'Enter Password'})

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ('title','description','thread_type')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'input is-medium', 'placeholder': 'Enter Username'})
        self.fields['description'].widget.attrs.update({'class':'textarea is-medium','rows': 4 ,'placeholder': 'Description'})
        self.fields['thread_type'].widget.attrs.update({'class':'input is-medium', 'placeholder': 'Enter Thread Type'})

class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields =('message',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'class':'textarea is-medium','rows': 4 ,'placeholder': 'Reply...'})
