from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Estas en la pagina principal de premios Platzi")


def detalle(request, question_id):
    return HttpResponse(F"Estas viendo la pregunta numero {question_id}")


def resultados(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta numero {question_id}")


def voto(request, question_id):
    return HttpResponse(f"Estas votado a la pregunta numero {question_id}")