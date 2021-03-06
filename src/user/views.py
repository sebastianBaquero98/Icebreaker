from django.shortcuts import render, redirect
from .models import MyUser

# Create your views here.
def acceso_view(request):
    request.get_host()
    if request.method == 'POST':
        nombre = request.POST['nombre']
        username = request.POST['username']
        if MyUser.objects.filter(username=username).exists():
            print("[EXCEPTION]: El username ya existe, no se creo en DB")
        else:
            user = MyUser.objects.create(nombre=nombre, username=username)
            user.save()
            print(f'Se creo el usuario {username} en la base de datos')
            
        return redirect('http://127.0.0.1:8000/frases/')
            
    else:
        return render(request, "acceso.html", {})

 