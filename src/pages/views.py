from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def frase_view(request):
    return render(request, "frase.html", {})
