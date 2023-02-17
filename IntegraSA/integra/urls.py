from django.urls import path
from integra import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name= "Home" ),
    path('search/', views.buscar, name= "Search"),
    path('categoria/', views.categoria ,name= "Categoria")
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)