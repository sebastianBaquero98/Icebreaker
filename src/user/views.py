from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def acceso_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "acceso.html", context)

 