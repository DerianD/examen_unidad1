from django.shortcuts import render 
from django.http import Http404
from django.shortcuts import get_object_or_404

from models import libromodelo


# Create your views here.

def home(request):
    mensaje="Bienvenido a la Bibioteca :D"
    send={"me":mensaje}
    return render(request, 'home.html',send) 


def lista_libros2(request):
    #Logico de negocio alias hechizo
    librosclass = libromodelo.objects.all()
    print request
    m = "libro nuevo"
    template = "lista_libros.html"
    contexto= {"mensaje":m,
               "libros": librosclass }
    return render(request, template, contexto)

def detalle_libro(request, object_id=None):
    #Logico de negocio alias hechizo
    librosclass2 = get_object_or_404(libromodelo, id=object_id)
    m = "libro nuevo"
    template = "detalleLibro.html"
    contexto= {"mensaje":m,
               "libros": librosclass2 }
    return render(request, template, contexto)

def detalle_s(request, slug=None):
    try:
        libroclass = get_object_or_404(libromodelo, slug=slug)
    except libromodelo.MultipleObjectsReturned:
        libroclass = libromodelo.objects.filter(slug=slug).order_by("-nombre").first()
    m = "libro nuevo"
    template = "detalle.html"
    contexto= {"mensaje":m,
           "producto": libroclass }
    return render(request, template, contexto)

def detalle_slug(request, slug=None):
    try:
        libroclass = get_object_or_404(libromodelo, slug=slug)
    except libromodelo.MultipleObjectsReturned:
        libroclass = libromodelo.objects.filter(slug=slug).order_by("-nombre").first()
    m = "libro nuevo"
    template = "detalle.html"
    contexto= {"mensaje":m,
           "producto": libroclass }
    return render(request, template, contexto)


