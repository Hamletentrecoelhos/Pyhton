from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Evento(models.Model):
    titulo = models.CharField(max_length=30)
    # CharFild é o título do campo.
    # max_length é o tamanho máximo de caracteres.
    descricao = models.TextField(blank=True, null=True)
    # blank -> dado pode ser branco (vasio); null=True -> o dado pode ser nulo.
    # Textfield -> tipo texto
    local = models.CharField(max_length=60)
    data_evento = models.DateTimeField(verbose_name='Data do evento:')
    # DateTimeField -> campo tipo data.
    # verbose_name -> redefine o nome da variável quando for aparecer no display.
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de criação:')
    # auto_now = dado é criado junto com o evento (criando na execução do código).
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # on_delete -> o que fazer quando um usuário for deletado, CASCATE para apagar tudo do usuário.

    # o comando abaixo é para dar o nome da tabela.
    class Meta:
        db_table = 'festanafloresta'

    # o comando abaixo embrulha a resposta na tela com outro str (nesse caso os eventos).
    def __str__(self):
        return self.titulo
    # o comando abaixo envolve a variável por uma redefinição
    # de seu formato de hora, por isso no arquivo html se pode ver:
    # get_data_evento e não data_evento.


    def get_data_evento(self):
        return self.data_evento


    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%d')

    def evento_atrasado(self):
        from datetime import datetime
        if self.data_evento < datetime.now():
            return True
        else:
            return False

    def get_hour(self):
        return self.data_evento.__str__()[11:]


