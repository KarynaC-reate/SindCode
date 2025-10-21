from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("<h1>Alô Django</h1>")
    return render(request, 'associados/index.html')
