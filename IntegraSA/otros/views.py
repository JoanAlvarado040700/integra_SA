from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, 'opc/contacto.html')

def about(request):
    return render(request, 'opc/about.html')

def empresa(request):
    return render(request, 'opc/buscar_empresa.html')