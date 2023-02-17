from django.urls import path
from registro import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_usuario, name= "Login_user" ),
    path('empresa/', views.login_empresa, name= "Login_empresa"),
    path('registro/', views.registro_usuario, name= "Registro_usuario"),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)