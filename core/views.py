from django.shortcuts import render
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, "core/index.html")

def home(request):
    return render(request,  "core/home.html")
    
def becas(request):
    return render(request,"core/becas.html")

def solicitar_orden(request):
    return render(request,"core/solicitar_orden.html")

def subir_comprobante(request):
    return render(request,"core/subir_comprobante.html")

