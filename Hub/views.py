from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from django import forms
from .models import Post
#from .forms import Post
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


# Create your views here.

def Hub(request):
    Hub = open("Plantillas/Hub.html")
    template = Template(Hub.read())
    Hub.close
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

'''def Boton_1(request):
    Boton_1 = open("Plantillas\Boton_1.html")
    template = Template(Boton_1.read())
    Boton_1.close
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)'''

def Boton_2(request):
    Boton_3 = open("Plantillas\Boton_3.html")
    template = Template(Boton_3.read())
    Boton_3.close
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

def Boton_3(request):
    Boton_4 = open("Plantillas\Boton_4.html")
    template = Template(Boton_4.read())
    Boton_4.close
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

def Boton_1(request):
    Boton_1 = open("Plantillas\Boton_1.html")
    template = Template(Boton_1.read())
    Boton_1.close
    posts = Post.objects.all()
    contexto = Context({
        'posts': posts
    })
    documento = template.render(contexto)
    return HttpResponse(documento)

@login_required
def create_post(request):
    crear = open("Plantillas\create_post.html")
    template = Template(crear.read())
    crear.close
    contexto = Context()
    documento = template.render(contexto)
    if request.method == 'POST':
        content = request.POST['content']
        if content:
            Post.objects.create(content=content)
            return redirect('create_post')
    return HttpResponse(documento)