from django.shortcuts import render, redirect
from .forms import AdminAuthenticationForm
from .forms import ConnexionForm
from django.contrib.auth import logout
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from utilisateur.models import User
from django.contrib.auth.views import redirect_to_login


def f():
    global var
    var = 1

def sign_in (request):
    form_admin = AdminAuthenticationForm()
    return render(request, 'connexion.html', locals())


def connexion(request):
    if request.user.is_authenticated():
        return redirect(reverse(index))

    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                request.session['current_user'] = username

                return redirect(reverse(index))

            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))


@login_required
def index(request):
    current_user = request.session['current_user']
    userdata = User.objects.get(username=current_user)
    if userdata.is_superuser:
        base = 'base_admin.html'
        return render(request, 'plainte/dashboard.html', locals())
    else:
        base = 'base.html'
        return render(request, 'plainte/dashboard.html', locals())



