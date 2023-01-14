from django.shortcuts import render
from .models import DemandInfo

# Create your views here.
def demand(request):
    demands = DemandInfo.objects.all()
    return render(request, 'demand/demand.html', {'demands': demands})
