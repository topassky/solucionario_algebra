from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from home.models import solucionario

# Create your views here.

class EjercicioListView(ListView):
    model = solucionario
    template_name = "home.html"
    context_object_name = 'my_favorite_publishers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lista = solucionario.objects.all()

        lista_nueva = []
        for i in range(0, len(lista), 4):
            lista_nueva.append(lista[i:i+4])

        data = {
            "ejercicios" : lista_nueva
        }

        context['ejercicios'] = lista_nueva
        context['listado_ejercicio'] = "Listado de ejercicios del algebra del Baldor"
        context['variable_auxiliar'] = "Enunciado"
        context['variable_auxiliar_2'] = "del"

        return context
