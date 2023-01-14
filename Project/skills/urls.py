from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.skills_home, name='skills_home')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)