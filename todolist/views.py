from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    todos = Todo.objects.all()

    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'todos':todos,'form':form}
    return render(request, 'todolist/list.html',context)

def updateTask(request,pk):
    todo = Todo.objects.get(id=pk)

    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}

    return render(request,'todolist/update_task.html',context)


def deleteTask(request,pk):
    item = Todo.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        #item.finish = True  
        #item.save()
        return redirect('/')

    context = {'item':item}
    return render(request,'todolist/delete.html',context)

