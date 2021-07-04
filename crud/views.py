from django.shortcuts import render,redirect
from .models import task
from .forms import taskform
# Create your views here.
def home(request):
	objectos = task.objects.all()
	form = taskform(request.POST or None)
	if form.is_valid():
		
		form.save()
	context = {'objectos':objectos,'form':form}	
	return render(request, 'home.html', context)

def delete(request, id):
	objecto = task.objects.get(id=id)
	objecto.delete()
	return redirect('home')

def update(request, id):
	objecto = task.objects.get(id=id)
	form = taskform(request.POST or None, instance=objecto)
	if form.is_valid():
		form.save()
		return redirect('home')
	context = {'form':form}
	return render(request, 'update.html', context)
	
	
	