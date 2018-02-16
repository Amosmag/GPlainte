from django.db import models

# Create your models here.


class Nationalite(models.Model):
    nationalite = models.CharField(max_length=50, verbose_name='Nationalite')

    def __str__(self):
        return self.nationalite


class Profession(models.Model):
    profession = models.CharField(max_length=100, verbose_name='Profession')

    def __str__(self):
        return self.profession


class Commune(models.Model):
    commune = models.CharField(max_length=50, verbose_name='Commune')

    def __str__(self):
        return self.commune


class Operateur(models.Model):
    operateur = models.CharField(max_length=50, verbose_name='Operateur')

    def __str__(self):
        return self.operateur


class Categorie(models.Model):
    categorie = models.CharField(max_length=50, verbose_name='categorie')

    def __str__(self):
        return self.categorie


class Canal(models.Model):
    canal = models.CharField(max_length=50, verbose_name='canal')

    def __str__(self):
        return self.canal


class ReferenceDossier(models.Model):
    numero = models.IntegerField(verbose_name='numero')
    libelle = models.CharField(max_length=50, verbose_name='libelle')

    pass


class ReferenceLigne(models.Model):
    numero = models.IntegerField(verbose_name='numero')
    libelle = models.CharField(max_length=50, verbose_name='libelle')

    pass


class Plaignant(models.Model):
    nom = models.CharField(max_length=50, verbose_name='Nom')
    prenoms = models.CharField(max_length=50, verbose_name='Prenoms')
    contact = models.CharField(max_length=30, verbose_name='Contect')
    adresse = models.CharField(max_length=100, verbose_name='Adresse')
    email = models.EmailField(max_length=50, verbose_name='Email')
    nationalite = models.ForeignKey(Nationalite, on_delete=models.CASCADE, verbose_name='Nationalite')
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, verbose_name='Profession')
    date_enregistrement = models.DateField(auto_now_add=True, verbose_name='date d"enregistrement')

    pass


class Calldata(models.Model):
    nom = models.CharField(max_length=50, verbose_name='Nom')
    prenoms = models.CharField(max_length=50, verbose_name='Prenoms')
    contact = models.CharField(max_length=30, null=True, verbose_name='Contact')
    nationnalite = models.CharField(max_length=50, null=True, verbose_name='Nationalite')
    operateur = models.ForeignKey(Operateur, on_delete=models.CASCADE, verbose_name='Operateur')
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, verbose_name='Profession')
    adresse = models.CharField(max_length=100, null=True, verbose_name='Adresse')
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, verbose_name='Commune')
    categorie_plainte = models.ForeignKey(Categorie, on_delete=models.CASCADE, verbose_name='Categorie')
    mail = models.EmailField(max_length=50, null=True, verbose_name='Email')
    telephone = models.CharField(max_length=30, verbose_name='Telephone')
    objet_appel = models.CharField(max_length=100, null=True, verbose_name='Objet')
    date_constat = models.DateField(verbose_name='date du constant', null=True)
    reference_fiche = models.CharField(max_length=100, unique=True, verbose_name='Reference')
    qualite_appel = models.CharField(max_length=50, null=True, verbose_name='Qualite appel')
    nature_appel = models.CharField(max_length=50, null=True, verbose_name='nature_appel')
    type_renseignement = models.CharField(max_length=50, null=True, verbose_name='type_renseignement')
    heure_appel = models.TimeField(null=True, verbose_name='heure_appel')
    langue_appel = models.CharField(max_length=20, null=True, verbose_name='langue_appel')
    action_entreprise = models.TextField(max_length=200, null=True, verbose_name='action_entreprise')
    reponse_operatrice = models.TextField(max_length=100, null=True, verbose_name='reponse_operatrice')
    suivi_plainte = models.CharField(max_length=50, null=True, verbose_name='suivi_plainte')
    enregistre_par = models.CharField(max_length=50, null=True, verbose_name='enregistre_par')
    recuperer = models.BooleanField(verbose_name='Recuperer', default=False)
    date_enregistrement = models.DateField(verbose_name='date enregistrement', null=True)

    pass


class Plainte(models.Model):
    reference = models.CharField(max_length=100, unique=True, verbose_name='Reference')
    nom = models.CharField(max_length=50, verbose_name='Nom')
    prenoms = models.CharField(max_length=50, verbose_name='Prenoms')
    contact = models.CharField(max_length=30, verbose_name='Contact')
    adresse = models.CharField(max_length=100, null=True, verbose_name='Adresse')
    email = models.EmailField(max_length=50, null=True, verbose_name='Email')
    nationalite = models.CharField(max_length=50, null=True, verbose_name='Nationalite')
    profession = models.CharField(max_length=50, null=True, verbose_name='Profession')
    date_prise_en_compte = models.DateField(verbose_name='date de prise en compte', null=True)
    etat_dossier = models.CharField(max_length=50, null=True, verbose_name='etat du dossier')
    instructeur = models.CharField(max_length=50, verbose_name='instructeur en charge')
    date_entree = models.DateField(verbose_name='date d"entree')
    date_sortie = models.DateField(verbose_name='date de sortie', null=True)
    analyses = models.TextField(verbose_name='analyses preliminaires', null=True)
    recommandations = models.TextField(verbose_name='recommandations', null=True)
    actions_entreprises = models.TextField(verbose_name='actions entreprises', null=True)
    resultats = models.TextField(verbose_name='resultats', null=True)
    decisions = models.CharField(max_length=300, null=True, verbose_name='decisions')
    conclusion = models.TextField(verbose_name='conclusion', null=True)
    autres_commentaires = models.TextField(verbose_name='autres commentaires', null=True)
    archive = models.CharField(max_length=100, verbose_name='archive', null=True)
    date_enregistrement = models.DateField(auto_now_add=True, verbose_name='date d"enregistrement')
    canal = models.ForeignKey(Canal, on_delete=models.CASCADE, verbose_name='canal')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, verbose_name='categorie')
    objet = models.TextField(verbose_name='objet de la plainte')
    delai_traitement = models.CharField(max_length=50, verbose_name='delai de traitement', null=True)
    operateur = models.ForeignKey(Operateur, on_delete=models.CASCADE, verbose_name='Operateur')
    date_constat = models.DateField(verbose_name='date du constant', null=True)
    annee = models.CharField(max_length=50, null=True, verbose_name='Annee')
    mois = models.CharField(max_length=50, null=True, verbose_name='Mois')

    pass



