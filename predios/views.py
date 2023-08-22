
from django.shortcuts import render, get_object_or_404, redirect
from .models import Predio
from .forms import PredioForm, PropietarioForm

def predios_list(request):
    predios = Predio.objects.all()
    return render(request, 'predios/predios_list.html', {'predios': predios})

def predio_create_edit(request, predio_id=None):
    predio = None
    if predio_id:
        predio = get_object_or_404(Predio, pk=predio_id)
    if request.method == 'POST':
        predio_form = PredioForm(request.POST, instance=predio)
        propietario_form = PropietarioForm(request.POST)  # Agrega el formulario de propietario
        if predio_form.is_valid() and propietario_form.is_valid():
            predio = predio_form.save(commit=False)
            predio.save()
            propietario = propietario_form.save()
            predio.propietarios.add(propietario)
            return redirect('predios_list')
    else:
        predio_form = PredioForm(instance=predio)
        propietario_form = PropietarioForm()  # Crea una instancia vacía del formulario de propietario
    return render(request, 'predios/predio_create_edit.html', {'predio_form': predio_form, 'propietario_form': propietario_form})

def predio_delete(request, predio_id):
    predio = get_object_or_404(Predio, pk=predio_id)
    if request.method == 'POST':
        predio.delete()
        return redirect('predios_list')
    return render(request, 'predios/predio_confirm_delete.html', {'predio': predio})
    return redirect('predios_list')
