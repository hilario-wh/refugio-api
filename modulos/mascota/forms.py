from django import forms
from modulos.mascota.models import Mascota


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota

        fields = [
            'image',
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]
        label = {
            'image': 'Imagen',
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad',
            'fecha_rescate': 'Fecha rescate',
            'persona': 'Adoptante',
            'vacuna': 'Vacunas',
        }
        widgets = {
            'image': forms.ClearableFileInput(),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class': 'form-control'}),
            'persona': forms.Select(attrs={'class': 'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }


class MascotaApiForm(forms.Form):
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sexo = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    edad_aproximada = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    fecha_rescate = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    persona = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    vacuna = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), required=False)
