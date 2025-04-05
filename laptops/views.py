from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Store, Laptop, Order
from .forms import LaptopForm, SearchForm, OrderForm

def index(request):
    stores = Store.objects.all()
    laptops = Laptop.objects.all()
    form = SearchForm(request.GET or None)
    if form.is_valid() and form.cleaned_data['query']:
        laptops = laptops.filter(name__icontains=form.cleaned_data['query'])
    return render(request, 'index.html', {'stores': stores, 'laptops': laptops, 'form': form})

def store_profile(request, pk):
    store = get_object_or_404(Store, pk=pk)
    laptops = Laptop.objects.filter(store=store)
    form = SearchForm(request.GET or None)
    if form.is_valid() and form.cleaned_data['query']:
        laptops = laptops.filter(name__icontains=form.cleaned_data['query'])
    return render(request, 'store_profile.html', {'store': store, 'laptops': laptops, 'form': form})

def laptop_detail(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            if laptop.stock >= quantity:
                order = Order.objects.create(
                    laptop=laptop,
                    quantity=quantity,
                    store=laptop.store
                )
                laptop.stock -= quantity
                laptop.save()
                return redirect('laptop_detail', pk=laptop.pk)
    else:
        form = OrderForm()
    return render(request, 'laptop_detail.html', {'laptop': laptop, 'form': form})

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
