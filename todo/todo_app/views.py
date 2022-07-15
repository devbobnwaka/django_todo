from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    query = request.GET.get('q')
    todo_qs = Todo.objects.all()
    if query is not None:
        todo_qs = Todo.objects.filter(todo__icontains=query)
    form = TodoForm()
    context = {
        'todos':todo_qs,
        'form':form,
    }
    if request.method == 'POST':
        form = TodoForm(request.POST)
        context['form'] = form
        if form.is_valid():
            try:
                new_todo = Todo.objects.create(todo=request.POST['todo']) 
                return redirect('/')
            except:
                pass
    return render(request, 'todo/index.html', context)

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')

def edit(request, pk):
    old_todo = Todo.objects.get(id=pk)
    context = {'todo': old_todo}
    if request.method == 'POST':
        old_todo.todo = request.POST['todo']
        old_todo.save()
        return redirect('/')
    return render(request, 'todo/edit.html', context)

