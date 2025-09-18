from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # process form (e.g., print or save)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            messages.success(request, 'Your message has been sent!')
            return redirect('contact')  # redirect to same page to clear form
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def faq(request):
    return render(request, 'faq.html')