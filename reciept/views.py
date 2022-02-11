from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Receipt


class ReceiptListView(ListView):
    model = Receipt
    fields = ['orders', 'price_all', 'discount_all']
    template_name = 'list_reciept.html'
