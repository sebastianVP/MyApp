from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template import loader
from django.shortcuts import render
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

class Persona(object):
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido= apellido



def nuevosaludo(request):
    #nombre= "Alexander"
    #apellido= "Valdez"
    p1 = Persona("Alexander Sebastian","Valdez")
    temasDelCurso=["Plantilla","Modelo","Formularios","Vistas","Despliegue"]
    #temasDelCurso=[]
    hora_actual = datetime.datetime.now()
    


    #doc_externo= open("/home/soporte/3RASESION/MyApp/Proyecto1/plantillas/miplantilla.html")
    #doc_externo = loader.get_template('miplantilla.html')
    #plt =  Template(doc_externo.read())
    #doc_externo.close()
    #ctx = Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":hora_actual,"temas":temasDelCurso})
    dict_ = {"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":hora_actual,"temas":temasDelCurso}
    #documento = doc_externo.render(dict)
    #documento =  plt.render(ctx)
    #return HttpResponse(documento)
    return render(request,"miplantilla.html",dict_)    


def electrodomesticos(request):
    fecha = datetime.datetime.now()
    return render(request,"electrodomesticos.html",{"fecha_hoy":fecha})



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
