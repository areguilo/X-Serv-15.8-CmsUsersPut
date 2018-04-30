from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pages
from django.views.decorators.csrf import csrf_exempt
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
        response += '<h2>Hi ' + request.user.username + ': <a href=http://localhost:8000/logout>logout</a></h2>'
        print(request.user.username)
    else:
        print('no')
        response += '<h2>Hi unknown client. Please <a href=http://localhost:8000/authenticate>login</a></h2>'
    return HttpResponse(response)


def loginpage(request):
    return HttpResponse("""<html><body><form action="/login" method = "POST">
    Username:<br>
    <input type="text" name='username' value=""><br>
    Password:<br>
    <input type="password" name='password' value=""><br>
    <input type="submit"value="login"></form></body></html>""")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('http://localhost:8000/')

@csrf_exempt
def my_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print ('usu: ' + username)
    print ('psw: ' + password)
    user = authenticate(username='root', password='root')
    print (user)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('http://localhost:8000/')
            # Redirect to a success page.
        else:
            response = 'Error: disables account <br><br><a href=http://localhost:8000/> Return to Main menu </a>'
            # Return a 'disabled account' error message
    else:
        response = 'Error: invalid login <br><br><a href=http://localhost:8000/> Return to Main menu </a>'
        # Return an 'invalid login' error message.
    return HttpResponse(response)

def contentPage(request, identifier):
    if request.method == "GET":
        if request.user.is_authenticated():
            try:
                object = Pages.objects.get(name = identifier)
                response = object.page + '<br><br><a href=http://localhost:8000/> Return to Main menu </a>'
            except Pages.DoesNotExist:
                response = "There are not pages for this object"
        else:
            response = '<h2>Information no available. Please <a href=http://localhost:8000/authenticate>login</a></h2>'
    else:
        page = Pages(name = identifier, page = request.body)
        page.save()
        response = page.name + "created"
    return HttpResponse(response)
