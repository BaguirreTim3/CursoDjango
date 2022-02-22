from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Questions


def index(request):
    latest_question_list = Questions.objects.all()
    return render(request, "polls/index.html", {
        'latest_question_list': latest_question_list
    } )

def detalle(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    print(question)
    return render(request, "polls/detalle.html", {
        'question': question
    })


def resultados(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta numero {question_id}")


def voto(request, question_id):
    return HttpResponse(f"Estas votado a la pregunta numero {question_id}")