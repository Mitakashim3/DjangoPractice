from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'productapp/home.html')
def add(request):
    context = {
        'message': ''
    }
    if request.method == 'GET':
        return render(request, 'productapp/add.html')
    if request.method == 'POST':
        prodname = request.POST.get('productname')
        prodprice = request.POST.get('productprice')
        # Save the product to the database
        product = Product(name=prodname, price=prodprice)
        product.save()
        context['message'] = prodname + ' added successfully'
        return render(request, 'productapp/add.html',{'message':'Product added successfully'})
    
def FetchAll(request):
    sortBy = request.GET.get('order_by', 'price')
    products = Product.objects.order_by(sortBy).filter(is_deleted=0)
    keyword =request.POST.get('keyword','')
    if keyword:
        products = products.filter(name__istartswith=keyword)
    context ={
        'tinitinda': products
    }
    return render(request, 'productapp/fetchall.html', context)

def update(request,uid):
    product = get_object_or_404(Product, id=uid)
    if request.method == 'GET':
        context = {
            'product': product
        }
        return render(request, 'productapp/edit.html', context)
    if request.method == 'POST':
        product.name = request.POST.get('productname')
        product.price = request.POST.get('productprice')
        product.save()
        return redirect('fetchall')

def hardDelete(request, uid):
    product = get_object_or_404(Product, id=uid)
    product.delete()
    return redirect('fetchall')

def softDelete(request, uid):
    product = get_object_or_404(Product, id=uid)
    product.is_deleted = 1
    product.save()
    return redirect('fetchall')
