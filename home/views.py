from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import SendContact
from .forms import ContactForm

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def contact(request):
    """ A view to return the contact page """

    return render(request, 'contact/contact.html')

def submit_contact(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = SendContact()
            data.user_id = request.user.id
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save()
            messages.success(request, 'Thank you! Your message has been sent!')
        else:
            messages.success(request, form.errors)
                
        return redirect(url)

def view_wishlist(request):
    """ A view that renders the wishlist contents page """
    # wishlist = Wishlist.objects.filter(user=request.user)
    # context = {'wishlist':wishlist}

    return render(request, 'wishlist/wishlist.html')
