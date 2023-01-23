from django.shortcuts import render,redirect
from .models import TodoItem
from todoApp.forms import TodoForm

# Create your views here.
def retrieve_view(request):
    todoitems = TodoItem.objects.all()
    context = {'todoitems':todoitems}
    return render(request,'todoApp/index.html',context)

def create_view(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')
    context = {'form':form }
    return render(request,'todoApp/create.html',context)

def update_view(request,id):
    todoitems = TodoItem.objects.get(id=id)  

    form= TodoForm(instance=todoitems)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance = todoitems)
        form.save()
        return redirect('/')
    return render(request,'todoApp/update.html',{'form':form})

def delete_view(request,id):
    todoitems = TodoItem.objects.get(id=id)  
    if request.method == 'POST':
        todoitems.delete()
        return redirect('/')
    return render(request,'todoApp/delete.html',{'todoitems':todoitems})
