from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Store, Laptop
from .forms import LaptopForm, SearchForm

def store_profile(request, pk):
    store = get_object_or_404(Store, pk=pk)
    laptops = Laptop.objects.filter(store=store)
    form = SearchForm(request.GET or None)
    if form.is_valid() and form.cleaned_data['query']:
        laptops = laptops.filter(name__icontains=form.cleaned_data['query'])
    return render(request, 'store_profile.html', {'store': store, 'laptops': laptops, 'form': form})

def laptop_detail(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    return render(request, 'laptop_detail.html', {'laptop': laptop})

class LaptopCreateView(CreateView):
    model = Laptop
    form_class = LaptopForm
    template_name = 'laptop_form.html'
    success_url = reverse_lazy('store_profile', kwargs={'pk': 1})

class LaptopUpdateView(UpdateView):
    model = Laptop
    form_class = LaptopForm
    template_name = 'laptop_form.html'
    success_url = reverse_lazy('store_profile', kwargs={'pk': 1})

class LaptopDeleteView(DeleteView):
    model = Laptop
    template_name = 'laptop_confirm_delete.html'
    success_url = reverse_lazy('store_profile', kwargs={'pk': 1})

def search_laptops(request):
    form = SearchForm(request.GET or None)
    laptops = Laptop.objects.all()
    if form.is_valid() and form.cleaned_data['query']:
        laptops = laptops.filter(name__icontains=form.cleaned_data['query'])
    return render(request, 'store_profile.html', {'form': form, 'laptops': laptops, 'store': Store.objects.first()})

def index(request):
    stores = Store.objects.all()
    return render(request, 'index.html', {'stores': stores})