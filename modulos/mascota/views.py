from django.shortcuts import render,redirect
from django.http import HttpResponse

from modulos.mascota.forms import MascotaForm
from modulos.mascota.models import Mascota
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

def index(request):
    return render(request, "mascota/function/index.html")


def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('mascota:function_mascota_listar')
    else:
        form = MascotaForm()
    return render(request, 'mascota/function/mascota_form.html', {'form':form})


def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas':mascota}
    return render(request, 'mascota/function/mascota_list.html', contexto)


def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method ==  'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, request.FILES, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:function_mascota_listar')
    return render(request, 'mascota/function/mascota_form.html', {'form':form})


def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:function_mascota_listar')
    return render(request, 'mascota/function/mascota_delete.html', {'mascota':mascota})


class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/class/mascota_list.html'


class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = "mascota/class/mascota_form.html"
    success_url = reverse_lazy('mascota:class_mascota_listar')


class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = "mascota/class/mascota_form.html"
    success_url = reverse_lazy('mascota:class_mascota_listar')


class MascotaDelete(DeleteView):
    model = Mascota
    template_name = "mascota/class/mascota_delete.html"
    success_url = reverse_lazy('mascota:class_mascota_listar')