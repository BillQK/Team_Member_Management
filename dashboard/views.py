from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
# request -> response 
# request handler 
# action 

#Landing Page 
def index(request):
    members =  Member.objects.all()
    
    context = {'members': members}
    return render(request, "dashboard/listpage.html", context)

#Add Member
def add(request):
    form = MemberForm()
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'form': form}
    return render(request, "dashboard/addpage.html", context)

# Edit Member using Primary Key 
def edit(request, pk): 
    member = Member.objects.get(id=pk)
    form = MemberForm(instance=member)
    
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'member': member, 'form' : form }
    return render(request, "dashboard/editpage.html", context)


# Delete Member using Primary Key
def delete(request, pk): 
    member = Member.objects.get(id=pk) 
    
    if request.method == "POST": 
        member.delete() 
        return redirect('/')
    
    context = {'member' : member}
    return render(request, 'dashboard/delete.html', context)