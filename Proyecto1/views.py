from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Alumnos estas es nuestra primera sesion del Curso")

def despedida(request):
    return HttpResponse("Este es el fin de la primera sesion del Curso")

