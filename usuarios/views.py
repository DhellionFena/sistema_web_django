from django.http import HttpResponse
from django.template import loader
from .models import User

def users(request):
    usuarios = User.objects.all().values()
    template = loader.get_template("lista_usuarios.html")

    contexto = {
        'usuarios': usuarios,
    }

    return HttpResponse(template.render(contexto, request))


def detalhes(request, id):
    usuario = User.objects.get(id=id)
    template = loader.get_template("detalhes.html")

    contexto = {
        "usuario": usuario,
        "idade": usuario.get_idade()
    }

    return HttpResponse(template.render(contexto, request))

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())