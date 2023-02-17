from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Publicaciones, Categoria, Departamento
# Create your views here.


def home(request ):

    pub = Publicaciones.objects.all()
    cat = Categoria.objects.all()
    dep = Departamento.objects.all()

    return render(request,'home/index.html',{'pub': pub, 'cat':cat, 'dep':dep} )

def categoria(request):
    #La variable cat y deb, estan conectadas a las tablas de categoria y departamentos. Por lo cual su funcion es que muestren los departamentos y categorias registrados en la base de datos 
    #cat = Categoria.objects.get(id = categoria_id)
    #dep = Departamento.objects.get(id = departamento_id)
    #pubCat = Publicaciones.objects.filter(categoria = cat)

    cat = Categoria.objects.all()
    dep = Departamento.objects.all()
    #id_cat = Categoria.objects.get(id)
    pub = Publicaciones.objects.all()

    if request.method == 'GET':
        cat_select = request.GET.get('categoria_select')
        dep_select = request.GET.get('dep_select')
        if cat_select != "" and dep_select == "":
            resul_cat = Publicaciones.objects.all().filter(categoria = cat_select)
            return render(request, 'home/categoria.html', {'resul': resul_cat, 'cat':cat, 'dep':dep, 'cat_select':cat_select}  )

        elif dep_select != "" and cat_select == "":
            resul_dep = Publicaciones.objects.all().filter(dep = dep_select)
            return render(request, 'home/categoria.html', {'resul': resul_dep, 'cat':cat, 'dep':dep, 'cat_select':cat_select}  )
        
        elif dep_select != "" and cat_select != "":
            resul_cat = Publicaciones.objects.all().filter(categoria = cat)
            resul_dep = Publicaciones.objects.all().filter(dep = dep_select)
            return render(request, 'home/categoria.html', {'resul': resul_dep, 'cat':cat, 'dep':dep, 'cat_select':cat_select, 'dep_select':dep_select})
        
        else:
            return render(request,'home/index.html',{'pub': pub, 'cat':cat, 'dep':dep} )



    #return 



def buscar(request):
    cat = Categoria.objects.all()
    dep = Departamento.objects.all()
    if request.method == 'GET':
        busqueda = request.GET.get('busqueda')
        resul = Publicaciones.objects.all().filter(titulo__icontains = busqueda) # Esta linea funciona como una sentencia sql Like
        return render(request,'home/search.html', {'resul': resul, 'cat':cat, 'dep':dep})
