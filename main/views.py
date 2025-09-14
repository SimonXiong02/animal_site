from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_vaild():
            # process form (e.g., print or save)
            print(form.cleaned_data)
            return render(request, 'contact.html', {'form': form, 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def faq(request):
    return render(request, 'faq.html')