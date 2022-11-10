from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
# request -> response 
# request handler 
# action 

def index(request):
    members =  Member.objects.all()
    
    context = {'members': members}
    return render(request, "dashboard/listpage.html", context)


def add(request):
    form = MemberForm()
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'form': form}
    return render(request, "dashboard/addpage.html", context)

def update(request, pk): 
    member = Member.objects.get(id=pk)
    return render(request, "dashboard/editpage.html")