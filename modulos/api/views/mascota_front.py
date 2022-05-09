import requests

from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render,redirect

from modulos.mascota.forms import MascotaForm
from modulos.mascota.models import Mascota
from django.core.urlresolvers import reverse_lazy
# Create your views here.

def get_api_response(url, request):
    try:
        response = requests.get(url, timeout=4, cookies=request.COOKIES)
        if response.status_code == 404:
            raise Http404("No encontrado")
    except:
        raise Http404("Error de conexion")
    return response

def front_mascota_list(request):
    url = '{}{}'.format(settings.DOMAIN, reverse_lazy('api:mascota_list_v1'))
    response = get_api_response(url, request)
    mascotas = response.json()
    contexto = {'mascotas':mascotas}
    return render(request, 'mascota/api/mascota_list.html', contexto)


def front_mascota_create(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('mascota:function_mascota_listar')
    else:
        form = MascotaForm()
    return render(request, 'mascota/function/mascota_form.html', {'form':form})


def front_mascota_edit(request, pk):
    mascota = Mascota.objects.get(pk=pk)
    if request.method ==  'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, request.FILES, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:function_mascota_listar')
    return render(request, 'mascota/function/mascota_form.html', {'form':form})


def front_mascota_delete(request, pk):
    url = '{}{}'.format(settings.DOMAIN, reverse_lazy('api:mascota_details_v1', kwargs={'pk': pk}))
    response = get_api_response(url, request)
    mascota = response.json()
    if request.method == 'POST':
        try:
            response = requests.delete(
                url,
                timeout=4,
                cookies=request.COOKIES,
                headers={
                    'X-CSRFToken': request.COOKIES.get('csrftoken')
                }
            )
            if response.status_code == 204:
                return redirect('api:api_mascota_listar')
        except:
            raise Http404("Error de conexion")
    return render(request, 'mascota/api/mascota_delete.html', {'mascota':mascota})