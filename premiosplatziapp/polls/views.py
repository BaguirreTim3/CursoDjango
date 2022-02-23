from django.shortcuts import get_object_or_404, render
from django.http import  HttpResponseRedirect
from django.urls import reverse
from .models import Choices, Questions

def index(request):
    latest_question_list = Questions.objects.all()
    return render(request, "polls/index.html", {
        'latest_question_list': latest_question_list
    } )

def detalle(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, "polls/detalle.html", {
        'question': question
    })


def resultados(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'polls/resultado.html', {
        'question': question
    })


def votos(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        select_choices = question.choices_set.get(pk=request.POST["choices"])
        print(select_choices)
    except (KeyError, Choices.DoesNotExist):
        return render(request, 'polls/detalle.html', {
            'question': question,
            'error_message': 'No elegistes una respuesta'
        })
    else:
        select_choices.votes += 1
        select_choices.save()
        return HttpResponseRedirect(reverse('polls:resultado', args=(question.id,)))    