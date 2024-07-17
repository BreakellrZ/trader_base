from django.shortcuts import render, redirect
from django.http import HttpResponse

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