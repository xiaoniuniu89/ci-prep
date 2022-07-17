from django.shortcuts import render
from allauth.account.forms import LoginForm

def landing(request):
    login_form = LoginForm()
    return render(request, 'index.html', {'form': login_form})
