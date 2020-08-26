from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # Constucting a dictionary to pass it as template's context
    context_dict = {'boldmessage': 'Some bullshit is written here'}

    # Returning a render response to sent to the client
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'creatorsname': 'Konstantin Popov'}

    return render(request, 'rango/about.html', context=context_dict)