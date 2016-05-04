from django import forms

class AuthenticationForm(forms.Form):
    """
    Login form
    """
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id': 'inputEmail',
                'class': 'form-control',
                'placeholder': 'Email address',
                'require': True,
                'autofocus': True,
            },
))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'inputPassword',
            'class': 'form-control',
            'placeholder': 'Password',
            'require': True,
        }))

    class Meta:
        fields = ['email', 'password']
