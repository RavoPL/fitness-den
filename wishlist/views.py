from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product, Wishlist

# Create your views here.

# Viewing the wishlist
def view_wishlist(request, user_id):
    """ A view that renders the wishlist contents page """
    # wishlist = Wishlist.objects.filter(user=request.user)
    # context = {'wishlist':wishlist}

    return render(request, 'wishlist/wishlist.html', context)

# Adding items to the wishlist
@login_required
def add_to_wishlist(request, item_id, user_id):
    """ Add a quantity of the specified product to the wishlist """

    if 'wishlist' in request.POST:
        product = get_object_or_404(Product, pk=item_id)
        redirect_url = request.POST.get('redirect_url')

        messages.info(request,'The item was added to your wishlist.')

        return redirect(redirect_url)


# Removing items from the wishlist
@login_required
def remove_from_wishlist(request, item_id, user_id):
    """ Remove the item from the wishlist """

    product = get_object_or_404(Product, pk=item_id)

    return redirect(redirect_url)
