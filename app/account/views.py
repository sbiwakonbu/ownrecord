from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.views.decorators.csrf import csrf_protect

from account.forms import AuthenticationForm

# Create your views here.
@csrf_protect
def login(request, template_name='login/index.jinja'):
    """
    Log in view
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('/profile')
    else:
        form = AuthenticationForm()
    return render(request, template_name, {
        'form': form,
    }, context_instance=RequestContext(request))

def logout_view(request):
    django_logout(request)
    return redirect('/')
