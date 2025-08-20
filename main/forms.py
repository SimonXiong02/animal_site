from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="NAME")
    email = forms.EmailField(label="EMAIL")
    message = forms.CharField(widget=forms.Textarea, label="MESSAGE")