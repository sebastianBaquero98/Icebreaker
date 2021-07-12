from django.shortcuts import render
from .models import Frase
import random
# Create your views here.
def frase_view(request):
    rands = random.sample(range(1,9), 3)
    #obj1 = Frase.objects.get(id=rands[0])
    #obj2 = Frase.objects.get(id=rands[1])
    #obj3 = Frase.objects.get(id=rands[2])

    #context = {
    #    'object1': obj1,
    #    'object2': obj2,
    #    'object3': obj3,
    #}
    
    return render(request, "frase.html", {})