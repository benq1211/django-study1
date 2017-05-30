from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect(request.GET.get('next','/'))
            ...
        else:
            return HttpResponse('Error',status=403)
            # Return an 'invalid login' error message.
    else:
        if request.user.is_authenticated:
            session = '.'.join(request.session.keys())    #获取session
            response = HttpResponse('session:%s' % session)
            return response
         #   return HttpResponse('have loging already')
        return render(request,'days/login.html')
# Return an 'invalid login' error message.

def logout_view(request):
    logout(request)
    return redirect('/days/login')
@login_required()
def index(request):
    return HttpResponse('this is index')