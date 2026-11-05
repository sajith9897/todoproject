# Create your views here.
from django.shortcuts import render
def greeting(request):
    count= 23
    return render(request,'index.html',{'x': count})

def greet(request):
    counts = '<b>23</b>'
    return render(request,'index.html',{'zx':counts})

def kick(request):
    count = 23
    return render(request,'index.html',{'l':count})

def joke(request):
    students = ['Ajay', 'Vineeth','Sudheesh']
    return render(request,'index.html',{'students':students})