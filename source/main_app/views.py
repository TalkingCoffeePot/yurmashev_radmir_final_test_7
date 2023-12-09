from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from main_app.models import GuestCard
from main_app.forms import GuestCardForm
# Create your views here.


def main_list(request):
    cards = GuestCard.objects.exclude(card_status='blocked').order_by('-date_create')
    context = {
        'cards': cards
    }
    return render(request, 'main_page.html', context)


def add_card(request):
    if request.method == 'GET':
        form = GuestCardForm()
        context = {
        'form': form
        }
        return render(request, 'add_card.html', context)
    elif request.method == 'POST':
        form = GuestCardForm(data=request.POST)
        if form.is_valid():
            GuestCard.objects.create(name=form.cleaned_data['name'], 
                                mail=form.cleaned_data['mail'], 
                                description=form.cleaned_data['description'])
            
            return redirect('cards')
        else:
            return render(request, 'new_card', context={'form': form})


def update_card(request, pk):
    card = GuestCard.objects.get(pk=pk) 
    if request.method == 'GET':
        form = GuestCardForm(initial={
            'name': card.name,
            'mail': card.mail,
            'description': card.description
        })
        context = {
            'card': card,
            'form': form
        }
        return render(request, 'update_card.html', context)
    elif request.method == 'POST':
        form = GuestCardForm(data=request.POST)
        if form.is_valid():
            card.name = form.cleaned_data['name']
            card.mail = form.cleaned_data['mail']
            card.description = form.cleaned_data['description']
            card.save()
            return redirect('cards')
        else:
            return render(request, 'update_card', context={'card': card,'form': form})


def delete_card(request, pk):
    card = GuestCard.objects.get(pk=pk) 
    if request.method == 'GET':
        return render(request, 'delete_card.html', context={'card': card})
    elif request.method == 'POST':
        card.delete()
        return redirect('cards')    

