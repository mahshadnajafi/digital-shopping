from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404

from shop.models import Product
from accounts.models import User
from orders.models import Order, OrderItem
from .forms import AddProductForm, AddCategoryForm, EditProductForm


def is_manager(user):
    try:
        if not user.is_manager:
            raise Http404
        return True
    except:
        raise Http404


@login_required
def index(request):
    return render(request,'dashboard.html')

@user_passes_test(is_manager)
@login_required
def home_dashb(request):
    return render(request,'dashboard.html', name='home')

# @user_passes_test(is_manager)
@login_required
def products(request):
    products = Product.objects.all()
    context = {'title':'Products' ,'products':products}
    return render(request, 'products.html', context)


@login_required
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New product added!')
            return redirect('dashboard:add_product')
    else:
        form = AddProductForm()
    context = {'title':'New Product', 'form':form}
    return render(request, 'add_product.html',context=context)



@login_required
def delete_product(request, id):
    product = Product.objects.filter(id=id).delete()
    messages.success(request, 'The product deleted', 'success')
    return redirect('dashboard:products')


@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product has been updated', 'success')
            return redirect('dashboard:products')
    else:
        form = EditProductForm(instance=product)
    context = {'title': 'Edit', 'form':form}
    return render(request, 'edit_product.html', context)

@login_required
def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New category added')
            return redirect('dashboard:add_category')
    else:
        form = AddCategoryForm()
    context = {'title':'Add a product category', 'form':form}
    return render(request, 'add_category.html', context)


@login_required
def orders(request):
    orders = Order.objects.all()
    context = {'title':'orders', 'orders':orders}
    return render(request, 'orders.html', context)


@login_required
def order_detail(request, id):
    order = Order.objects.filter(id=id).first()
    items = OrderItem.objects.filter(order=order).all()
    context = {'title':' order details', 'items':items, 'order':order}
    return render(request, 'order_detail.html', context)