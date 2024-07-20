from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Checkbox
from .forms import ListForm


# View checklist
@login_required
def list(request):
    """
    Display Checklist
    Each user sees their own checklist
    """
    checklist = Checkbox.objects.filter(author=request.user)
    form = ListForm()

    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            checkbox = form.save(commit=False)
            checkbox.author = request.user
            checkbox.save()
        return redirect('/tradingcheck/list/')

    context = {'checklist': checklist, 'form': form}
    return render(request, 'list_checkbox.html', context)


# View to update checklist inputs
def updateList(request, pk):
    """
    When user clickes update, goes to update_list.html.
    Can update from there.
    Displays update message once redirected back to /tradingcheck/list page.
    """
    list = Checkbox.objects.get(id=pk)

    form = ListForm(instance=list)

    if request.method == 'POST':
        form = ListForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Checklist Updated!')
            return redirect('/tradingcheck/list/')

    context = {'form': form}

    return render(request, 'update_list.html', context)


# View to delete checklist inputs
def deleteList(request, pk):
    """
    When user clicks delete button,
    Goes to delete.html page, where users can delete an input.
    Displays delete message once redirected back to /tradingcheck/list page.
    """
    item = Checkbox.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        messages.add_message(
            request, messages.SUCCESS, 'Checklist input deleted!')
        return redirect('/tradingcheck/list/')

    context = {'item': item}
    return render(request, 'delete.html', context)
