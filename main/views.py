from django.shortcuts import render, redirect
from .models import EventDetails 
from .forms import EventsForm
from base64 import b64encode
from django.contrib import messages

def homepage(request):
    data = EventDetails.objects.all()
    return render(request = request, template_name = "main/home.html", context = {'data':data})

def events(request):
    form = EventsForm()
    if request.method == 'POST':
        form = EventsForm(request.POST)        
        if form.is_valid():
            form.save()
            messages.success(request, "Added to Events!")
            context = {'form':form}
            return redirect('main:homepage')
        else:
            messages.error(request, "Invalid. Try Again.")
    context = {'form':form}
    return render(request, 'main/addevents.html', context)
