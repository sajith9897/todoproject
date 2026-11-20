from django.shortcuts import render, redirect
from .forms import ProductForm
from .forms import Product

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =ProductForm()
    return render(request, 'create.html', {'form': form})

def product_read(request):
    product_list=Product.objects.all()
    return render(request,'retrieve.html',{'product_list':product_list})

def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =ProductForm(instance=product)           
    return render(request, 'update.html', {'form': form})

from django.shortcuts import render
def product_delete(request,pk):
    product=Product.objects.get(pk=pk)  
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    
    return render(request,'delete.html',{'product':product})


# Listing page with pagination

from django.core.paginator import Paginator

def listing(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 3)  # Set the number of items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj})