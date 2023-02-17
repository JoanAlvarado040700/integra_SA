from django.shortcuts import render

# Create your views here.

def login_usuario(request):

    return render(request, 'usuario/login.html')

def login_empresa(request):
    return render(request, 'empresa/login.html')

def registro_usuario(request):
    """
    Aqui haremos una condicional para no hacer tantos registros, 
    solo que en cada situacion no redirecciones a otro archivo html
    de registro. Empresa y usuario comun
    """
    return render(request, 'usuario/registro.html')