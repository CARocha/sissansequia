from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('sequias.views',
    (r'^index/$', 'consultar'),
    (r'^descargar/xls/$', 'hoja_calculo_xls'),
    (r'^perdida/$', 'perdidapostrera'),
    (r'^perdida/grafos/$', 'grafo_perdida'),
    (r'^disponibilidad/$', 'disponibilidad'),
    (r'^disponibilidad/grafos/$', 'grafo_disponibilidad'),
    (r'^nutricion/$', 'nutricion'),
    (r'^nutricion/grafos/$', 'grafo_nutricion'),
    (r'^ajax/municipio/(?P<departamento>\d+)/$', 'get_municipios'),
    (r'^ajax/comunidad/(?P<municipio>\d+)/$', 'get_comunidad'),
    (r'^ajax/entrevista/(?P<comunidad>\d+)/$', 'get_entrevista'),
)
