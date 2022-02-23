from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detalle"),
    path("<int:pk>/resultados/", views.ResultView.as_view(), name="resultado"),
    path("<int:question_id>/votos/", views.votos, name="votos"),
]
