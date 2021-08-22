from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('becas/', views.becas, name="becas"),
    path('solicitar_orden/', views.solicitar_orden, name="solicitar_orden"),
    path('subir_comprobante/', views.subir_comprobante, name="subir_comprobante"),
    
]