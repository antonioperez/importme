from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json

def Home(request):
    return render(request, 'importme/base.html')


def Login(request):
    response= {}
    response['message'] = 'Invalid Username or password'
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                response['message'] = 'Login Successful'
                return JsonResponse(response, status=200)
            else: 
                response['message'] = 'User account disabled'

        return JsonResponse(response, status=400)
    else:
        return redirect('/user/login/')

def Logout(request):
    logout(request)
    response['message'] = 'Logged out'
    return JsonResponse(response, status=200)