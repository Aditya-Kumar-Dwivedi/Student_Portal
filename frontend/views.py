from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request,*args,**kwargs):
    return render(request,'frontend/index.html')
def not_found(request,exception):
    return render(request, 'frontend/index.html',status=404)
def icon(request):
    return HttpResponse("Icon")
