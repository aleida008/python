from django.http import HttpResponse

lista = ["fiorela", "camila" ,"vanessa", "sofia"]

def listar(request):
    return HttpResponse(lista)

def saludar(request):
    return HttpResponse( f"Bienvenido al curso de Python con Django")

def saludar_nombre(request, nombre):
    texto = f"hola {nombre}"
    return HttpResponse(texto)

def factorial(request, numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado = resultado * i

    return HttpResponse(f"El factorial de {numero} es {resultado}")

from django.shortcuts import render 
def inicio_render(request):
    return render(request, 'app1/inicio.html')
