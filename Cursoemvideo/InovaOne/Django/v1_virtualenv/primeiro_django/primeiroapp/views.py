from django.shortcuts import render, HttpResponse
from datetime import date
# Create your views here.


def hello(request, nome):
    return HttpResponse(f'<h1>Olá, mundo! No dia {date.today()}!</h1> Olá, {nome}. Bem vindo a mais uma tentativa minha de passar disso...')
