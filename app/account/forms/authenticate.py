from django import forms

class AuthenticationForm(forms.Form):
    """
    Login form
    """
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'inputUsername',
                'class': 'form-control',
                'placeholder': 'Username',
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
        fields = ['username', 'password']
