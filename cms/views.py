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


changeContentForm = """<html><body><form action="" method = "POST"><br>
<input type="text" name='content' value=""><br>
<input type="submit"value="change content"></form></body></html>"""
@csrf_exempt
def contentPage(request, name):
    if request.method == "GET":
        try:
            object = Pages.objects.get(name = name)
            response = "<h2>The page's content is: </h2>" + object.page + '<br><br><a href=http://localhost:8000/> Return to Main menu </a><br>'
        except Pages.DoesNotExist:
            response = "There are not pages for this object"
        if request.user.is_authenticated():
            response += '<h3>Change content:</h3>' + changeContentForm
    else:
        object = Pages.objects.get(name = name)
        object.page = request.POST['content']
        object.save()
        response = 'Actualised page<br><a href=http://localhost:8000/> Return to Main menu </a><br> \
        <a href=http://localhost:8000/' + name + '> Go to ' + name + "'s page </a>"
    return HttpResponse(response)
