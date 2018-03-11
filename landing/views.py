from django.shortcuts import render, redirect
from .forms import SubscribersForm

# Create your views here.

def landing(request):
    form = SubscribersForm(request.POST or None)
    if  request.method == "POST" and form.is_valid():
        new_form = form.save()
        return redirect('landing/landing.html')
    return render(request, 'landing/landing.html', locals())