from django.http import HttpResponse
import datetime
from django.template import Template,Context
#def saludo(request):
#    return HttpResponse("Hola Alumnos estas es nuestra primera sesion del Curso")

def saludo(request):
     documento="""<html>
     <body>
     <h1>
      Hola Alumnos esta es nuestra segunda sesion del Curso
     </h1>
     </body>
     </html>"""
     return HttpResponse(documento)

def nuevosaludo(request):
    doc_externo= open("/home/soporte/ProyectoPython/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    plt =  Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento =  plt.render(ctx)
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Este es el fin de la primera sesion del Curso")

def obtenerFecha(request):

    fecha_actual = datetime.datetime.now() 
    documento="""<html>
    <body>
    <h1>
    Fecha y Hora Actual %s
    </h1>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)


def calcularEdad(request,agno):
    edadActual =  33
    periodo     = agno -2023
    edadFutura  =  periodo + edadActual
    documento   =  "<html><body><h2>En el año %s tendras %s años</h2></body></html>"%(agno,edadFutura)
    return HttpResponse(documento)
