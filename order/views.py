from django.shortcuts import render
from seller.models import Food
from .models import Cart
from django.db.models import Sum
# Create your views here.

def order_detail(request, pk) :
    food = Food.objects.get(pk=pk)
    context = {
        'object' : food
    }
    return render(request, 'order/order_detail.html', context)

from django.http import JsonResponse
def modify_cart(request) :
    user = request.user
    food_id = request.POST['foodId']
    food = Food.obejcts.get(pk=food_id)
    cart, created = Cart.objects.get_or_create(food = food, user = user)
    cart.amount += int(request.POST['amountChange'])
    
    if cart.amount > 0:
        cart.save()

    totalQuantity = user.cart_set.aggregate(totalcount=Sum('amount'))['totalcount']
    #Json
    context = {
        'newQuantity' : cart.amount,
        'totalQuantity' : totalQuantity,
        'message' : 'success',
        'success' : True
    }

    return JsonResponse(context)