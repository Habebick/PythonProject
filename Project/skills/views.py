from django.shortcuts import render
from .models import Mainskills


# Create your views here.
def skills_home(request):
    skills = Mainskills.objects.all()
    return render(request, 'skills/skills_home.html', {'skills': skills})
