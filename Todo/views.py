from django.shortcuts import render,redirect
from .models import TodoItem

# Create your views here.
def todoview(request):
    a = TodoItem.objects.all()
    return render(request,'ui.html',{'a':a})

def todoadd(request):
    if request.method == 'POST':
        c = request.POST['content']
        new = TodoItem(content = c)
        new.save()
        a = TodoItem.objects.all()
        return render(request, 'ui.html', {'a': a})
