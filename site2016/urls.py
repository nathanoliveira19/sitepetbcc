from django.conf.urls import url
from site2016 import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^manutencao/$', views.manutencao, name='manutencao'),
    url(r'^equipe/$', views.equipe, name='equipe'),
    url(r'^equipe/(?P<id>[0-9]{1,3})/$', views.membro, name='membro'),
    url(r'^projetos/$', views.projetos, name='projetos'),
    url(r'^projetos/(?P<id>[0-9]{1,3})/$', views.projeto, name='projeto'),
    url(r'^processoseletivo/(?P<ano>[0-9]{4})/(?P<semestre>[0-9]{1})/$', views.processo_seletivo, name='processo_seletivo'),
    url(r'^contato/$', views.contato, name='contato'),
]
