from django.shortcuts import render
from .forms import ContactForm

#from django.core.mail import EmailMessage, send_mail
#from django.shortcuts import redirect
#from django.template.loader import get_template
# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    context = {
        'form': form,
    }   
    return render(request, 'contact.html', context)