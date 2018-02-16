from .models import Plainte
from utilisateur.models import User
from datetime import datetime
from gplainte.views import connexion
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.backends.db import SessionStore


def encour(request):
    encours_admin = Plainte.objects.filter(etat_dossier='En cours de traitement').count()
    data = Plainte.objects.filter(etat_dossier='En cours de traitement')
    return {'encours_admin': encours_admin, 'data': data}


def total(request):
    totale = Plainte.objects.all().count()
    affecter = Plainte.objects.filter(instructeur='').count()
    return {'total': totale, 'affecter': affecter}


def cemois(request):
    ce_mois = Plainte.objects.filter(annee=datetime.today().year, mois=datetime.today().month).count()

    return {'cemois': ce_mois}


def operateur(request):
    mtn = Plainte.objects.filter(operateur__operateur='MTN').count()
    moov = Plainte.objects.filter(operateur__operateur='MOOV').count()

    try:
        current_user = request.session['current_user']
        userdata = User.objects.get(username=current_user)

        if userdata.is_superuser:
            plaintedb = Plainte.objects.all()
            encours = Plainte.objects.filter(etat_dossier='En cours de traitement').exclude(instructeur='').count()
            cloture = Plainte.objects.filter(etat_dossier='Cloturé').count()
            totale = Plainte.objects.all().count()
            return {'mtn': mtn, 'moov': moov, 'plaintedb': plaintedb, 'current_user': current_user, 'encours': encours,
                    'cloture': cloture, 'totale': totale}
        else:
            plaintedb = Plainte.objects.filter(instructeur=userdata.nom_prenoms)
            encours = Plainte.objects.filter(etat_dossier='En cours de traitement', instructeur=userdata.nom_prenoms).count()
            cloture = Plainte.objects.filter(etat_dossier='Cloturé', instructeur=userdata.nom_prenoms).count()
            totale = Plainte.objects.filter(instructeur=userdata.nom_prenoms).count()
            return {'mtn': mtn, 'moov': moov, 'plaintedb': plaintedb, 'current_user': current_user, 'encours': encours,
                    'cloture': cloture, 'totale': totale}
    except:
        return {'mtn': mtn, 'moov': moov}



