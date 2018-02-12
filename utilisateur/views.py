from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from utilisateur.models import User
from utilisateur.forms import UserForm, ImageUploadForm
from django.views.generic import UpdateView, DeleteView
from gplainte.views import index
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import csv, datetime
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseForbidden


# Create your views here.
def liste(request):
    titre = "Utilisateur"
    etat = "active"
    disp = "block"
    object_list = User.objects.all()

    return render(request, 'utilisateur/liste.html', locals())


def create(request):
    titre = "Trafic"
    etat_trafic = "active"
    disp_trafic = "block"

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        """username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        profession = request.POST['profession']
        fonction = request.POST['fonction']
        photo = request.FILES['file']
        #photo_name = request.POST['photo_name']

        user = User.objects.create_user(username, email=email, password=password, first_name=first_name,
                                        last_name=last_name, profession=profession, fonction=fonction, photo=photo, )"""
        if form.is_valid():
            #form.cleaned_data['nom_prenoms'] = nom_prenoms = form.cleaned_data['last_name'] + ' ' + form.cleaned_data['first_name']
            form.save()
            u = User.objects.get(username=form.cleaned_data['username'])
            u.set_password(form.cleaned_data['password'])
            u.save()
        return redirect(liste)
    else:
        form = UserForm
        return render(request, 'utilisateur/create.html', locals())


class Update(UpdateView):

    model = User
    titre = "Trafic"
    template_name = 'utilisateur/_update_form.html'
    form_class = UserForm
    success_url = reverse_lazy(liste)


class Delete(DeleteView):
    model = User
    context_object_name = "utilisateur"
    template_name = 'utilisateur/supprimer.html'
    success_url = reverse_lazy(liste)


def profil(request, pk):
    form = UserForm
    #var = User.objects.filter(username='user.username')
    utilisateur = User.objects.get(id=pk)
    if request.method == 'POST':
        u = User.objects.get(id=pk)
        u.set_password(request.POST['password'])
        u.save()
        return redirect(index)
    current_user = request.session['current_user']
    userdata = User.objects.get(username=current_user)
    if userdata.is_superuser:
        base = 'base_admin.html'
        return render(request, 'utilisateur/profil.html', locals())
    else:
        base = 'base.html'
        return render(request, 'utilisateur/profil.html', locals())