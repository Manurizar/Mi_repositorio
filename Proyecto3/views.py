from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime 
from django.template import loader

def template(self):
    plantilla = loader.get_template("plantillas_final.html")

    documento = plantilla.render()

    return HttpResponse(documento)
