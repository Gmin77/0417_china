from django.shortcuts import render, redirect
from .models import Food
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

# Create your views here.

@login_required
def seller_index(request) :
    food = Food.objects.all().filter(user__id=request.user.id)
    context ={
        'object_list' : 'hello'
    }
    return render(request, 'seller/seller_index.html')

def add_food(request) :
    if request.method=='GET':
        return render(request, 'seller/seller_add_food.html')
    # post
    elif request.method=="POST":
        # 폼에서 전달되는 각 값을 뽑아와서 DB에 저장

        # Food 내용을 구성 영역
        # category = Category.objects.get(name=request.POST['category'])
        user=request.user
        food_name = request.POST['name']
        food_price = request.POST['price']
        food_description = request.POST['description']

        # 이미지 저장 및 url 설정 내용
        fs=FileSystemStorage()
        uploaded_file = request.FILES['file']
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)

        Food.objects.create(user= user,name=food_name, price =food_price , description=food_description,image_url=url)    

        # food_name, price, description
        return redirect('seller:seller_index')
    
def food_detail(request, pk) :
    Food.objects.get(pk=pk)
    context ={
        'object' : Food
    }
    return render(request, 'seller/seller_food_detail.html', context)

def food_delete(reuqest) :
    pass