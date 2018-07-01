from django import forms
from .models import Plaignant, Plainte, Operateur, Nationalite, Profession


class NationaliteForm(forms.ModelForm):
    class Meta:
        model = Nationalite
        fields = '__all__'


class ProfessionForm(forms.ModelForm):
    class Meta:
        model = Profession
        fields = '__all__'


class OperateurForm(forms.ModelForm):
    class Meta:
        model = Operateur
        fields = '__all__'


class PlaignantForm(forms.ModelForm):
    class Meta:
        model = Plaignant
        fields = '__all__'


class PlainteForm(forms.ModelForm):
    class Meta:
        model = Plainte
        fields = '__all__'


class TraitementForm(forms.ModelForm):
    class Meta:
        model = Plainte
        fields = 'analyses', 'recommandations', 'actions_entreprises', 'resultats', 'decisions', 'conclusion' \
            , 'autres_commentaires', 'archive'

