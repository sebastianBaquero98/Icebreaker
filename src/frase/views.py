from django.shortcuts import render
from .models import Frase
import random
# Create your views here.
def frase_view(request):
    randNum = random.randrange(1,9)
    obj = Frase.objects.get(id=randNum)

    context = {
        'object': obj
    }
    
    return render(request, "frase.html", context)