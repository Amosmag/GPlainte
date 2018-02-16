from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    #url(r'^$', views.liste, name="liste"),
    url(r'^liste$', views.liste, name="liste_utilisateur"),
    url(r'^profil/(?P<pk>\d+)$', views.profil, name="profil"),
    url(r'^create$', views.create, name="nouveau_utilisateur"),
    url(r'^edit/(?P<pk>\d+)$', views.Update.as_view(), name='update_utilisateur'),
    url(r'^supprimer/(?P<pk>\d+)$', views.Delete.as_view(), name='delete_utilisateur'),
    #url(r'^importer$', views.importation, name="importation"),
    #url(r'^import$', views.charger, name="import"),
    #url(r'^export/(?P<queryset>\w+)$', views.export, name='export'),
    #url(r'^export/(?P<annee>\d+)/(?P<mois>\d+)/(?P<operateur>\d+)/(?P<categorie>\d+)/(?P<source>\d+)$', views.export, name='export'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)