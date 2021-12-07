from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from .models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import Http404, JsonResponse


# Create your views here.


#def index(request):
#    return redirect('/agenda/')

def festa(request, eventos):
    try:
        local = Evento.objects.get(titulo=eventos)
        return HttpResponse(f'<h1>{eventos}</h1>{local}')
    except:
        return HttpResponse(f'O evento {eventos} não existe.')

def login_user(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido.")
    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def agenda(request):
    from datetime import datetime, timedelta
    # Use request.x(o que você quer pegar da sessão requisitada).
    usuario = request.user
    # A definição do dicionário abaixo parace ser requisito necessário
    # para a utilização de código python no arquivo html lido pelo django
    # sendo que o único link que precisa se manter entre o cod. html e a
    # definição em views é o nome que se dá ao elemento no dicionário
    # nesse caso (eventos).
    # Talvez ainda haja outras formas de fazer isso.
    deven = {'eventos': Evento.objects.filter(usuario=usuario, data_evento__gt=datetime.now() - timedelta(days=2))}
    # Acima você também pode usar a opção "filter" (no caso acrescentando -> usuario=usuario) ao invés de all
    # para que a página apresente conteúdo personalizado para cada usuário.
    # Use __gt ou __lt, após uma variável de filter, para dizer que quer filtrar números >= ou <= à variável entregue.
    return render(request, 'agenda.html', deven)


@login_required(login_url='/login/')
def evento(request):
    tmp = {}
    if request.GET.get('id'):
        tmp['evento'] = Evento.objects.get(id=request.GET.get('id'))
        # definindo um dicionário para adicionar o id nos dados da url (quando esse já houver)
    return render(request, 'evento.html', tmp)


@login_required(login_url='/login/')
def salvar_evento(request):
    if request.POST:
        if request.POST.get('id_evento'):
            if Evento.objects.get(id=request.POST.get('id_evento')).usuario == request.user:
                # Evento.objects.filter(id=request.POST.get('id_evento')).update(titulo=request.POST.get('titulo'),
                # data_evento=request.POST.get('Data'), descricao=request.POST.get('descricao'))
                even = Evento.objects.get(id=request.POST.get('id_evento'))
                even.titulo = request.POST.get('titulo')
                even.data_evento = request.POST.get('Data') + ' ' + request.POST.get('Hour') + ':00'
                print(even.data_evento)
                even.decricao=request.POST.get('descricao')
                even.save()
                # SAVE TAMBÉM ALTERA OS DADOS COMO update()
        else:
            Evento.objects.create(titulo=request.POST.get('titulo'), data_evento=request.POST.get('Data'),
                                  descricao=request.POST.get('descricao'), usuario=request.user)
    return redirect('/')


@login_required(login_url='/login/')
def deletar_evento(request, id_evento):
    try:
        devento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    if devento.usuario == request.user:
        devento.delete()


    return redirect('/')


def json_lista_evento(request, id_usuario):
    from datetime import datetime, timedelta
    try:
        usuario = User.objects.get(id=id_usuario)
        return JsonResponse(list(Evento.objects.filter(usuario=usuario).values('id', 'titulo',)), safe=False)
    except:
        return HttpResponse('Não foi achado um evento com esse id.')
