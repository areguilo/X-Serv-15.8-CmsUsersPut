from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def mainPage(request):
    list = Pages.objects.all()
    response = '<ul><h2>'
    for item in list:
        print(item.name)
        response = response + '<li><a href=http://localhost:8000/' + str(item.name) + ">" + item.name + '</a></li>'
    response = response + '</ul></h2>'
    response = "<h1>Hi!, these are our contents managed:</h1>" + response
    if request.user.is_authenticated():
        response += '<h2>Hi ' + request.user.username + '</h2>'
        print(request.user.username)
    else:
        print('no')
        response += '<h2>Hi unknown client. Please <a href=http://localhost:8000/login>login</a></h2>'
    return HttpResponse(response)

def loginPage(request):
    return HttpResponse("""<form action="" method = "POST">
    Username:<br>
    <input type="text" name='username' value=""><br>
    Password:<br>
    <input type="password" name='password' value=""><br>
    <input type="submit"value="Enviar"></form>""")


def contentPage(request, identifier):
    if request.method == "GET":
        if request.user.is_authenticated():
            try:
                object = Pages.objects.get(name = identifier)
                response = object.page + '<br><br><a href=http://localhost:8000/> Return to Main menu </a>'
            except Pages.DoesNotExist:
                response = "There are not pages for this object"
        else:
            response = '<h2>Information no available. Please <a href=http://localhost:8000/login>login</a></h2>'
    else:
        page = Pages(name = identifier, page = request.body)
        page.save()
        response = page.name + "created"
    return HttpResponse(response)
