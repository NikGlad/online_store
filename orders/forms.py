from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name',  # 'last_name', 'email',
                  'telephone',
                  # 'postal_code',
                  'address']
