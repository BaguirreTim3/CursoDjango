from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detalle, name="index"),
    path("<int:question_id>/resultados/", views.resultados, name="index"),
    path("<int:question_id>/voto/", views.voto, name="index"),
]
