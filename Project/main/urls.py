from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name ="home"),
    path('about', views.skills, name ="skills"),
    path('hh/', include('hh.urls')),
    path('skills/', include('skills.urls')),
    path('demand/', include('demand.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)