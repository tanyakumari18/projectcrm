from django.shortcuts import render, redirect
from .forms import ProductForm, CreateUserForm
from account.models import Order, Customer, Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def register_view(request):
    form = CreateUserForm()
    context = {'form': form}
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')
    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.method == "POST":
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')

        user = authenticate(username=username1, password=password1)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfully')
            return redirect('home')
        else:
            messages.warning(request, 'Username or Password is Wrong')
    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def Home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = len(orders)
    pending_orders = orders.filter(status='Pending').count()
    delivered_orders = orders.filter(status='Delivered').count()
    outfordelivery_orders = orders.filter(status='Outfordelivery').count()

    context = {'orders': orders,
               'customers': customers,
               'total_orders': total_orders,
               'pending_orders': pending_orders,
               'delivered_orders': delivered_orders,
               'outfordelivery_orders': outfordelivery_orders}

    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'accounts/product.html', context)


@login_required(login_url='login')
def order(request):
    return render(request, 'accounts/order.html')


@login_required(login_url='login')
def customer(request, pk):
    customers = Customer.objects.get(id=pk)
    fullname = customers.first_name + " " + customers.last_name
    orders = customers.order_set.all()

    total_orders = len(orders)
    pending_orders = orders.filter(status='Pending').count()
    delivered_orders = orders.filter(status='Delivered').count()
    outfordelivery_orders = orders.filter(status='Outfordelivery').count
    context = {'customers': customers,
               'orders': orders,
               'fullname': fullname,
               'total_orders': total_orders,
               'pending_orders': pending_orders,
               'delivered_orders': delivered_orders,
               'outfordelivery_orders': outfordelivery_orders
               }
    return render(request, 'accounts/customer.html', context)


@login_required(login_url='login')
def all_customers(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'accounts/all_customers.html', context)


@login_required(login_url='login')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product')
    else:
        form = ProductForm()
        contex = {'form': form}
        return render(request, 'accounts/add_product.html', contex)


@login_required(login_url='login')
def edit_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    context = {'form': form}

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/product')
    else:
        return render(request, 'accounts/edit_product.html', context)


@login_required(login_url='login')
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('/product')


def logout_view(request):
    logout(request)
    return redirect('login')
