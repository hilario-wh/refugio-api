import json
import requests

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import render,redirect

from modulos.mascota.forms import MascotaApiForm
from django.core.urlresolvers import reverse_lazy


def format_url(url):
    url = '{}{}'.format(settings.DOMAIN, url)
    return url


def get_api_response(request, url):
    try:
        url = format_url(url)
        response = requests.get(url, timeout=4, cookies=request.COOKIES)
    except:
        raise Http404("Error de conexion")
    if response.status_code == 404:
        raise Http404("No encontrado")
    if response.status_code == 403:
        raise PermissionDenied("No permitido")
    return response


def format_options(source, key, value):
    options = []
    for option in source:
        options.append((option.get(key), option.get(value)))
    return options


def front_mascota_list(request):
    response = get_api_response(request, reverse_lazy('api:mascota_list_v1'))
    mascotas = {}
    if response.status_code == 200:
        mascotas = response.json()
    contexto = {'mascotas':mascotas}
    return render(request, 'mascota/api/mascota_list.html', contexto)


def format_form_post(form):
    post_data = {}
    for field in form.data:
        if field == 'vacuna':
            post_data[field] = form.data.getlist(field)
        else:
            data = form.data.get(field, "")
            if data != "":
                post_data[field] = data
    post_data['vacuna'] = post_data.get("vacuna", [])
    return json.dumps(post_data)


def front_mascota_create(request):
    if request.method == 'POST':
        try:
            form = MascotaApiForm(request.POST)
            post_data = format_form_post(form)
            response = requests.post(
                format_url(reverse_lazy('api:mascota_list_v1')),
                timeout=4,
                cookies=request.COOKIES,
                headers={
                    'Content-Type': 'application/json',
                    'X-CSRFToken': request.COOKIES.get('csrftoken')
                },
                data=post_data
            )
            if response.status_code == 400 or response.status_code == 302:
                return redirect('api:api_mascota_crear')
            return redirect('api:api_mascota_listar')
        except:
            raise Http404("Error de conexion")

    else:
        form = MascotaApiForm()

        personas = get_api_response(request, reverse_lazy('api:persona_list'))
        personas = format_options(personas.json(), "id", "nombre")

        vacunas = get_api_response(request, reverse_lazy('api:vacuna_list'))
        vacunas = format_options(vacunas.json(), "id", "nombre")

        form.fields['persona']._set_choices(personas)
        form.fields['vacuna']._set_choices(vacunas)

    return render(request, 'mascota/api/mascota_form.html', {'form':form})


def front_mascota_edit(request, pk):
    if request.method == 'POST':
        try:
            form = MascotaApiForm(request.POST)
            post_data = format_form_post(form)
            response = requests.put(
                format_url(reverse_lazy('api:mascota_details_v1', kwargs={'pk': pk})),
                timeout=4,
                cookies=request.COOKIES,
                headers={
                    'Content-Type': 'application/json',
                    'X-CSRFToken': request.COOKIES.get('csrftoken')
                },
                data=post_data
            )
            if response.status_code == 400 or response.status_code == 302:
                return redirect('api:api_mascota_crear')
            return redirect('api:api_mascota_listar')
        except:
            raise Http404("Error de conexion")
        return redirect('mascota:function_mascota_listar')
    else:
        response = get_api_response(request, reverse_lazy('api:mascota_details_v1', kwargs={'pk': pk}))
        mascota = response.json()

        personas = get_api_response(request, reverse_lazy('api:persona_list'))
        personas = format_options(personas.json(), "id", "nombre")

        vacunas = get_api_response(request, reverse_lazy('api:vacuna_list'))
        vacunas = format_options(vacunas.json(), "id", "nombre")

        if mascota["persona"] is not None:
            mascota["persona"] = mascota.get("persona").get("id")

        if mascota["vacuna"] is not None:
            mascota["vacuna"] = [vacuna.get("id") for vacuna in mascota.get("vacuna")]

        form = MascotaApiForm(data=mascota)

        form.fields['persona']._set_choices(personas)
        form.fields['vacuna']._set_choices(vacunas)

    return render(request, 'mascota/function/mascota_form.html', {'form':form})


def front_mascota_delete(request, pk):
    response = get_api_response(request, reverse_lazy('api:mascota_details_v1', kwargs={'pk': pk}))
    mascota = response.json()
    if request.method == 'POST':
        try:
            response = requests.delete(
                format_url(reverse_lazy('api:mascota_details_v1', kwargs={'pk': pk})),
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