from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from .utils import cookieCart, cartData

def store(request):

    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all() 
    context = {'products':products, 'cartItems':cartItems}
    return render(request,"store.html", context)


def buyPage(request,id):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all() 
    product = Product.objects.get(id=id)
    context = {'products':products, 'cartItems':cartItems, 'product':product}
    return render(request,"buyPage.html",context)


def cart(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,"cart.html", context)


def checkout(request):
    
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,"checkout.html", context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('productId',productId)
    print('Action',action)

    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer=customer,complete = False)
    
    orderItem, created = Orderltem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
         
    orderItem.save()

    if orderItem.quantity <= 0:
         orderItem.delete()
            
    return JsonResponse('Item was added', safe=False)