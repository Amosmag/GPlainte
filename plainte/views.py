from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import NationaliteForm, ProfessionForm, PlaignantForm, PlainteForm, TraitementForm
from django.contrib.auth.decorators import login_required
from .models import Plainte, ReferenceDossier, Canal, Operateur, Calldata
from utilisateur.models import User
import datetime
import timestring
from django.views.generic import UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.utils import timezone

# Create your views here.


@login_required
def dashboard(request):
    current_user = request.session['current_user']
    userdata = User.objects.get(username=current_user)
    ligne = Plainte.objects.filter(canal__canal='Ligne verte').count()
    site = Plainte.objects.filter(canal__canal='Site web').count()
    courrier = Plainte.objects.filter(canal__canal='Courrier').count()
    email = Plainte.objects.filter(canal__canal='Email').count()
    if userdata.is_superuser:
        base = 'base_admin.html'
        return render(request, 'plainte/dashboard.html', locals())
    else:
        base = 'base.html'
        return render(request, 'plainte/dashboard.html', locals())


def Nouveau_nationalite(request):
    Nationalite_form = NationaliteForm

    return render(request, 'plainte/Nouveau_dossier.html', locals())

def Nouveau_profession(request):
    Profession_form = ProfessionForm

    return render(request, 'plainte/Nouveau_dossier.html', locals())


def Nouveau_plaignant(request):
    Plaignant_form = PlaignantForm

    return render(request, 'plainte/Nouveau_dossier.html', locals())


@login_required
def nouveau_dossier(request):
    ref = ReferenceDossier.objects.all().count()
    num = ref + 1
    reference = ('ARCEP/' + timestring.Date(datetime.date.today()).year.__str__() + '/' + timestring.Date(
        datetime.date.today()).month.__str__() + '/' + num.__str__())
    plainte_form = PlainteForm
    if request.method == "POST":
        reference = request.POST['reference']
        nom = request.POST["nom"]
        prenoms = request.POST["prenoms"]
        contact = request.POST["contact"]
        adresse = request.POST["adresse"]
        profession = request.POST["profession"]
        nationalite = request.POST["nationalite"]
        email = request.POST["email"]
        date_entree = request.POST["date_entree"]
        canal = request.POST["canal"]
        operateur = request.POST["operateur"]
        categorie = request.POST["categorie"]
        objet = request.POST["objet"]
        date_constat = request.POST["date_constat"]
        analyses = request.POST["analyses"]
        recommandations = request.POST["recommandations"]
        actions_entreprises = request.POST["actions_entreprises"]
        resultats = request.POST["resultats"]
        decisions = request.POST["decisions"]
        conclusion = request.POST["conclusion"]
        autres_commentaires = request.POST["autres_commentaires"]
        #instructeur = request.POST["instructeur"]
        date_enregistrement = datetime.date.today()
        mois = request.POST["mois"]
        annee = request.POST["annee"]
        #mois = timestring.Date(datetime.date.today()).month
        #annee = timestring.Date(datetime.date.today()).year
        date = timestring.Date(datetime.date.today()).date

        plainte = Plainte()
        plainte.nom = nom
        plainte.prenoms = prenoms
        plainte.profession = profession
        plainte.nationalite = nationalite
        plainte.contact = contact
        plainte.adresse = adresse
        plainte.email = email
        plainte.date_entree = date_entree
        plainte.canal_id = canal
        plainte.operateur_id = operateur
        plainte.categorie_id = categorie
        plainte.objet = objet
        plainte.date_constat = date_constat
        plainte.analyses = analyses
        plainte.recommandations = recommandations
        plainte.resultats = resultats
        plainte.actions_entreprises = actions_entreprises
        plainte.decisions = decisions
        plainte.conclusion = conclusion
        plainte.autres_commentaires = autres_commentaires
        plainte.reference = reference
        plainte.etat_dossier = 'Non affecté'
        #plainte.instructeur = instructeur
        plainte.annee = annee
        plainte.mois = mois
        plainte.save()

        ReferenceDossier.objects.create(numero=num, libelle=reference)

        return redirect(dashboard)
    mois = timestring.Date(datetime.date.today()).month
    annee = timestring.Date(datetime.date.today()).year
    current_user = request.session['current_user']
    userdata = User.objects.get(username=current_user)
    if userdata.is_superuser:
        base = 'base_admin.html'
        return render(request, 'plainte/Nouveau_dossier.html', locals())
    else:
        base = 'base.html'
        return render(request, 'plainte/Nouveau_dossier.html', locals())


#def ouvrir(request):

    #return render(request, 'plainte/ouvrir.html', locals())


class Ouvrir(UpdateView):

    model = Plainte
    titre = "Plainte"
    template_name = 'plainte/ouvrir.html'
    form_class = PlainteForm
    success_url = reverse_lazy(dashboard)


def encours(request):
    current_user = request.session['current_user']
    userdata = User.objects.get(username=current_user)
    if userdata.is_superuser:
        base = 'base_admin.html'
        liste_encours = Plainte.objects.filter(etat_dossier='En cours de traitement').exclude(instructeur='')
        return render(request, 'plainte/encours.html', locals())
    else:
        base = 'base.html'
        liste_encours = Plainte.objects.filter(etat_dossier='En cours de traitement', instructeur=userdata.nom_prenoms)
        return render(request, 'plainte/encours.html', locals())


def dossiers_cloture(request):
    current_user = request.session['current_user']
    userdata = User.objects.get(username=current_user)
    if userdata.is_superuser:
        base = 'base_admin.html'
        liste_cloture = Plainte.objects.filter(etat_dossier='Cloturé')
        return render(request, 'plainte/cloture.html', locals())
    else:
        base = 'base.html'
        liste_cloture = Plainte.objects.filter(etat_dossier='Cloturé', instructeur=userdata.nom_prenoms)
        return render(request, 'plainte/cloture.html', locals())


'''class Traitement(UpdateView):
    model = Plainte
    titre = "Traitement"
    template_name = 'plainte/ouvrir.html'
    form_class = TraitementForm
    success_url = reverse_lazy(dashboard)'''


def traitement(request, pk):
    etat1 = 'class="complete"'
    etat2 = 'class="active"'
    form = Plainte.objects.get(id=pk)
    if request.method == 'POST':

        form.instructeur = request.POST["instructeur"]
        form.analyses = request.POST["analyses"]
        form.recommandations = request.POST["recommandations"]
        form.resultats = request.POST["resultats"]
        form.actions_entreprises = request.POST["actions_entreprises"]
        form.decisions = request.POST["decisions"]
        form.conclusion = request.POST["conclusion"]
        form.autres_commentaires = request.POST["autres_commentaires"]
        form.save()
        return redirect(dashboard)
    current_user = request.session['current_user']
    userdata = User.objects.get(username=current_user)
    if userdata.is_superuser:
        base = 'base_admin.html'
        return render(request, 'plainte/_update_form.html', locals())
    else:
        base = 'base.html'
        return render(request, 'plainte/_update_form.html', locals())


def liste(request):
    liste_plainte = Plainte.objects.all()
    utilisateur = User.objects.all()
    return render(request, 'plainte/admin/liste.html', locals())


def liste_a_affecter(request):
    liste_plainte = Plainte.objects.filter(instructeur='')
    utilisateur = User.objects.all()
    return render(request, 'plainte/admin/liste_a_affecter.html', locals())


def affectation(request, pk):
    form = Plainte.objects.get(id=pk)
    if request.method == 'POST':
        form.instructeur = request.POST['nom_prenoms']
        form.etat_dossier = 'En cours de traitement'
        form.save()

        return redirect(liste)
    return redirect(liste)


def cloture(request, pk):
    form = Plainte.objects.get(id=pk)
    form.etat_dossier = 'Cloturé'
    form.save()

    return redirect(dashboard)


def recherche(request):
    if request.method == 'GET':
        var = request.GET['q']
        object_list = Plainte.objects.filter(Q(reference__icontains=var) | Q(operateur__operateur__icontains=var) |
                                             Q(nom__icontains=var) | Q(prenoms__icontains=var) | Q(canal__canal__icontains=var) |
                                             Q(instructeur=var) | Q(objet__icontains=var) | Q(categorie__categorie__icontains=var) |
                                             Q(contact__icontains=var) | Q(etat_dossier__icontains=var))
        current_user = request.session['current_user']
        userdata = User.objects.get(username=current_user)
        if userdata.is_superuser:
            base = 'base_admin.html'
            return render(request, 'plainte/recherche.html', locals())
        else:
            base = 'base.html'
            return render(request, 'plainte/recherche.html', locals())

    #return render(request, 'plainte/recherche.html', locals())


def graphe_par_operateur(request):
    current_user = request.session['current_user']
    userdata = User.objects.get(username=current_user)
    if userdata.is_superuser:
        base = 'base_admin.html'
        return render(request, 'plainte/graphe/graphe_par_operateur.html', locals())
    else:
        base = 'base.html'
        return render(request, 'plainte/graphe/graphe_par_operateur.html', locals())


def total_par_operateur(request):
    current_user = request.session['current_user']
    userdata = User.objects.get(username=current_user)
    if userdata.is_superuser:
        base = 'base_admin.html'
        return render(request, 'plainte/graphe/total_par_operateur.html', locals())
    else:
        base = 'base.html'
        return render(request, 'plainte/graphe/total_par_operateur.html', locals())


def graphe_par_categorie(request):
    current_user = request.session['current_user']
    userdata = User.objects.get(username=current_user)
    if userdata.is_superuser:
        base = 'base_admin.html'
        return render(request, 'plainte/graphe/graphe_par_categorie.html', locals())
    else:
        base = 'base.html'
        return render(request, 'plainte/graphe/graphe_par_categorie.html', locals())


def graphe_par_canal(request):
    current_user = request.session['current_user']
    userdata = User.objects.get(username=current_user)
    ligne = Plainte.objects.filter(canal__canal='Ligne verte').count()
    site = Plainte.objects.filter(canal__canal='Site web').count()
    courrier = Plainte.objects.filter(canal__canal='Courrier').count()
    email = Plainte.objects.filter(canal__canal='Email').count()
    if userdata.is_superuser:
        base = 'base_admin.html'
        return render(request, 'plainte/graphe/graphe_par_canal.html', locals())
    else:
        base = 'base.html'
        return render(request, 'plainte/graphe/graphe_par_canal.html', locals())


def graphe_par_dossier(request):
    current_user = request.session['current_user']
    userdata = User.objects.get(username=current_user)
    if userdata.is_superuser:
        base = 'base_admin.html'
        return render(request, 'plainte/graphe/graphe_par_dossier.html', locals())
    else:
        base = 'base.html'
        return render(request, 'plainte/graphe/graphe_par_dossier.html', locals())


def charger_ligne(request):
    current_user = request.session['current_user']
    userdata = User.objects.get(username=current_user)
    object_list = Calldata.objects.filter(nature_appel='Plainte', recuperer=False)
    if userdata.is_superuser:
        base = 'base_admin.html'
        return render(request, 'plainte/ligne_verte.html', locals())
    else:
        base = 'base.html'
        return render(request, 'plainte/ligne_verte.html', locals())


def recuperer(request, pk):
    ref = ReferenceDossier.objects.all().count()
    data = Calldata.objects.get(id=pk)
    num = ref + 1
    reference = ('ARCEP/' + timestring.Date(datetime.date.today()).year.__str__() + '/' + timestring.Date(datetime.date.today()).month.__str__() + '/' + num.__str__())

    plainte = Plainte()
    plainte.nom = data.nom
    plainte.prenoms = data.prenoms
    plainte.profession = data.profession
    plainte.nationalite = data.nationnalite
    plainte.contact = data.contact
    plainte.adresse = data.adresse
    plainte.email = data.mail
    plainte.date_entree = timestring.Date(datetime.date.today()).date
    plainte.canal_id = 1
    plainte.operateur_id = data.operateur_id
    plainte.categorie_id = data.categorie_plainte_id
    plainte.objet = data.objet_appel
    plainte.date_constat = data.date_constat
    plainte.reference = reference
    plainte.etat_dossier = 'Non affecté'
    plainte.annee = timestring.Date(datetime.date.today()).year
    plainte.mois = timestring.Date(datetime.date.today()).month
    plainte.save()

    data.recuperer = True
    data.save()

    ReferenceDossier.objects.create(numero=num, libelle=reference)
    return redirect(charger_ligne)
