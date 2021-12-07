from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello, World! Again... O_O')

def ola_querido(request, name):
    import re
    from django.utils.timezone import datetime
    from django.http import HttpResponse

    agora_formatado = datetime.now().strftime('%d de %b de %Y às %X')
    nome_limpo = str()
    
    objeto_ligavel = re.match("[a-zA-Z]+", name)

    if objeto_ligavel:
        nome_limpo = objeto_ligavel.group(0)
    else:
        nome_limpo = "Amigo"
    
    return HttpResponse(f'Olá, {nome_limpo}! É {agora_formatado}.')

