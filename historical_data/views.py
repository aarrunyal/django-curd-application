from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import ModelForm

from historical_data.models import PriceHistory
# Create your views here.

class PriceHistoryForm(ModelForm):
    class Meta:
        model = PriceHistory
        fields = ['date', 'price', 'volume']
        
def price_history_list(request, template = 'price_history/price_history_list.html'):
    price_history = PriceHistory.objects.all()
    data = {}
    data['object_list'] = price_history
    return render(request, template, data)

def price_history_view(request, pk, template_name='price_history/price_history_detail.html'):
    book= get_object_or_404(PriceHistory, pk=pk)    
    return render(request, template_name, {'object':book})

def price_history_create(request, template_name='price_history/price_history_form.html'):
    form = PriceHistoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('price_history_list')
    return render(request, template_name, {'form':form})

def price_history_update(request, pk, template_name='price_history/price_history_form.html'):
    book= get_object_or_404(PriceHistory, pk=pk)
    form = PriceHistoryForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('price_history_list')
    return render(request, template_name, {'form':form})

def price_history_delete(request, pk, template_name='price_history/price_history_delete.html'):
    book= get_object_or_404(PriceHistory, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('price_history_list')
    return render(request, template_name, {'object':book})
    