import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.http import JsonResponse

from .forms import ContactsForm, QuizForm, CommentsForm
from .models import Quiz


# Create your views here.


def teste_page_views(requests):
    return HttpResponse('oisfhgghvbn')


def teste2_page_views(requests, name):
    return HttpResponse(f'ola, {name} !')


def home_page_views(request):
    context = {'hora': datetime.datetime.now().hour}
    return render(request, 'parte2/home.html', context)


def about_page_views(request):
    return render(request, 'parte2/about.html')


def index_page_views(requests):
    return render(requests, 'parte2/index.html')


def bottas_page_views(requests):
    return render(requests, 'parte2/bottas.html')


def romeo_page_views(requests):
    return render(requests, 'parte2/alfa-romeo.html')


def alonso_page_views(requests):
    return render(requests, 'parte2/alonso.html')


def tauri_page_views(requests):
    return render(requests, 'parte2/alphatauri.html')


def alpine_page_views(requests):
    return render(requests, 'parte2/alpine.html')


def aston_page_views(requests):
    return render(requests, 'parte2/aston-martin.html')


def ferrari_page_views(requests):
    return render(requests, 'parte2/ferrari.html')


def gasly_page_views(requests):
    return render(requests, 'parte2/gasly.html')


def giovinazzi_page_views(requests):
    return render(requests, 'parte2/giovinazzi.html')


def haas_page_views(requests):
    return render(requests, 'parte2/haas.html')


def hamilton_page_views(requests):
    return render(requests, 'parte2/hamilton.html')


def latifi_page_views(requests):
    return render(requests, 'parte2/latifi.html')


def leclerc_page_views(requests):
    return render(requests, 'parte2/leclerc.html')


def mazepin_page_views(requests):
    return render(requests, 'parte2/mazepin.html')


def mclaren_page_views(requests):
    return render(requests, 'parte2/mclaren.html')


def mercedes_page_views(requests):
    return render(requests, 'parte2/mercedes.html')


def norris_page_views(requests):
    return render(requests, 'parte2/norris.html')


def ocon_page_views(requests):
    return render(requests, 'parte2/ocon.html')


def perez_page_views(requests):
    return render(requests, 'parte2/perez.html')


def raikkonen_page_views(requests):
    return render(requests, 'parte2/raikkonen.html')


def redbull_page_views(requests):
    return render(requests, 'parte2/red-bull.html')


def ricciardo_page_views(requests):
    return render(requests, 'parte2/ricciardo.html')


def russel_page_views(requests):
    return render(requests, 'parte2/russell.html')


def sainz_page_views(requests):
    return render(requests, 'parte2/sainz.html')


def shumacher_page_views(requests):
    return render(requests, 'parte2/schumacher.html')


def standings_page_views(requests):
    return render(requests, 'parte2/standings.html')


def strollpage_views(requests):
    return render(requests, 'parte2/stroll.html')


def tsunoda_page_views(requests):
    return render(requests, 'parte2/tsunoda.html')


def verstappen_page_views(requests):
    return render(requests, 'parte2/verstappen.html')


def vettel_page_views(requests):
    return render(requests, 'parte2/verstappen.html')


def williams_page_views(requests):
    return render(requests, 'parte2/williams.html')


def contact_form_page_views(requests):
    return render(requests, 'parte2/contactsForm.html')


def quiz_form_page_views(requests):
    return render(requests, 'parte2/quizz.html')


def comments_form_page_views(requests):
    return render(requests, 'parte2/comments.html')


def quiz_nota_page_views(requests):
    context = {"respostas": Quiz.objects.all()}
    return render(requests, 'parte2/quizNota.html', context)


def contacts_create_view(request):
    form = ContactsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('index'))
    context = {
        'form': form
    }
    return render(request, 'parte2/contactsForm.html', context)


def quiz_create_view(request):
    form = QuizForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('quizNota'))
    context = {
        'form': form
    }
    return render(request, 'parte2/quizz.html', context)


def comments_create_view(request):
    form = CommentsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('index'))
    context = {
        'form': form
    }
    return render(request, 'parte2/comments.html', context)
