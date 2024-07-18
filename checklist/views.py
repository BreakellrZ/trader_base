from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Checkbox
from .forms import ListForm

# Create your views here.

def list(request):
    checklist = Checkbox.objects.all()

    form = ListForm()

    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/tradingcheck/list/')

    context = {'checklist': checklist, 'form': form}
    return render(request, 'list_checkbox.html', context)

def updateList(request, pk):
    list = Checkbox.objects.get(id=pk)

    form = ListForm(instance=list)

    if request.method == 'POST':
        form = ListForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('/tradingcheck/list/')

    context = {'form' : form}

    return render(request, 'update_list.html', context)

def deleteList(request, pk):
    item = Checkbox.objects.get(id=pk)

    context = {'item' : item}
    return render(request,'delete.html', context )