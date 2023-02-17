from django.urls import path
from otros import views
urlpatterns = [
    path('about/', views.about, name="About"),
    path('contactar/', views.contact, name="Contacto"),
    path('buscar_empresa/', views.empresa, name="Buscar_empresa")

]
