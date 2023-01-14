from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/my_index.html', data)

def skills(request):
    return render(request, 'skills/skills_home.html')

def demand(request):
    return render(request, 'demand/demand.html')