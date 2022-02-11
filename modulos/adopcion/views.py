from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from modulos.adopcion.models import Solicitud, Persona
from modulos.adopcion.forms import SolicitudForm, PersonaForm

# Create your views here.


def index(request):
    return HttpResponse('index de adopcion')


def solicitud_list(request):
    solicitud = Solicitud.objects.all()
    contexto = {'solicitudes': solicitud}
    return render(request, 'adopcion/function/solicitud_list.html', contexto)


def solicitud_view(request):
    if request.method == 'POST':
        form_solicitud = SolicitudForm(request.POST)
        form_persona = PersonaForm(request.POST)
        if form_solicitud.is_valid() and form_persona.is_valid():
            solicitud = form_solicitud.save(commit=False)
            solicitud.persona = form_persona.save()
            solicitud.save()
        return redirect('adopcion:function_solicitud_listar')
    else:
        form_solicitud = SolicitudForm()
        form_persona = PersonaForm();
        context = {
            'form': form_solicitud,
            'form2': form_persona
        }
        return render(request, 'adopcion/function/solicitud_form.html', context)


def solicitud_update(request, solicitud_id):
    solicitud = Solicitud.objects.get(id=solicitud_id)
    persona = Persona.objects.get(id=solicitud.persona_id)
    if request.method == 'GET':
        form_solicitud = SolicitudForm(instance=solicitud)
        form_persona = PersonaForm(instance=persona)
        context = {
            'form': form_solicitud,
            'form2': form_persona,
        }
    else:
        form_solicitud = SolicitudForm(request.POST, instance=solicitud)
        form_persona = PersonaForm(request.POST, instance=persona)
        if form_solicitud.is_valid() and form_persona.is_valid():
            form_persona.save()
            form_solicitud.save()
        return redirect('adopcion:function_solicitud_listar')
    return render(request, 'adopcion/function/solicitud_form.html', context)


def solicitud_delete(request, solicitud_id):
    solicitud = Solicitud.objects.get(id=solicitud_id)
    if request.method == 'POST':
        solicitud.delete()
        return redirect('adopcion:function_solicitud_listar')
    return render(request, 'adopcion/function/solicitud_delete.html')


class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopcion/class/solicitud_list.html'


class SolicitudCreate(CreateView):
    model = Solicitud
    template_name = 'adopcion/class/solicitud_form.html'
    form_class = SolicitudForm
    second_class_form = PersonaForm
    success_url = reverse_lazy('adopcion:class_solicitud_listar')

    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_class_form(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_class_form(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class SolicitudUpdate(UpdateView):
    model = Solicitud
    second_model = Persona
    template_name = 'adopcion/class/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('adopcion:class_solicitud_listar')

    def get_context_data(self, **kwargs):
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        solicitud_id = kwargs['pk']
        solicitud = self.model.objects.get(id=solicitud_id)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        form = self.form_class(request.POST, instance=solicitud)
        form2 = self.second_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())


class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name = 'adopcion/class/solicitud_delete.html'
    success_url = reverse_lazy('adopcion:class_solicitud_listar')