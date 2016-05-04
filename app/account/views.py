from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import login as django_login, authenticate, logout as django_logout

from account.forms import AuthenticationForm, RegistrationForm

# Create your views here.
def login(request, template_name='login/index.jinja'):
    """
    Log in view
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, template_name, {
        'form': form,
    }, context_instance=RequestContext(request))

def register(request, template_name='register/index.jinja'):
    """
    User registration view.
    """
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'register/index.jinja', {
        'form': form,
    }, context_instance=RequestContext(request))
