from django import forms
from .models import Wishlist

# WishlistForm for custom Wishlist model
class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['product', 'user']