from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^Nouveau_dossier$', views.nouveau_dossier, name="Nouveau_dossier"),
    url(r'^ouvrir/(?P<pk>\d+)$', views.Ouvrir.as_view(), name='ouvrir'),
    url(r'^encours$', views.encours, name="encours"),
    url(r'^traitement/(?P<pk>\d+)$', views.traitement, name="traitement"),
    url(r'^liste$', views.liste, name='liste'),
    url(r'^liste_a_affecter$', views.liste_a_affecter, name='liste_a_affecter'),
    url(r'^affecter/(?P<pk>\d+)$', views.affectation, name='affecter'),
    url(r'^cloturer/(?P<pk>\d+)$', views.cloture, name='cloture'),
    url(r'^recherche$', views.recherche, name='recherche'),
    url(r'^dossiers_cloture$', views.dossiers_cloture, name='dossiers_cloture'),
    url(r'^graphe_par_operateur$', views.graphe_par_operateur, name='graphe_par_operateur'),
    url(r'^graphe$', views.total_par_operateur, name='total_par_operateur'),
    url(r'^graphe_par_categorie$', views.graphe_par_categorie, name='graphe_par_categorie'),
    url(r'^graphe_par_canal$', views.graphe_par_canal, name='graphe_par_canal'),
    url(r'^graphe_par_dossier$', views.graphe_par_dossier, name='graphe_par_dossier'),
    url(r'^ligne_verte$', views.charger_ligne, name='ligne_verte'),
    url(r'^recuperer/(?P<pk>\d+)$', views.recuperer, name='recuperer'),
    #url(r'^supprimer/(?P<pk>\d+)$', views.Delete.as_view(), name='delete_utilisateur'),
    #url(r'^importer$', views.importation, name="importation"),
    #url(r'^import$', views.charger, name="import"),
    #url(r'^export/(?P<queryset>\w+)$', views.export, name='export'),
    #url(r'^export/(?P<annee>\d+)/(?P<mois>\d+)/(?P<operateur>\d+)/(?P<categorie>\d+)/(?P<source>\d+)$', views.export, name='export'),
]
#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)