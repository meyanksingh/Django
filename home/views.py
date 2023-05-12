from django.shortcuts import render,HttpResponse,redirect
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def index(request):  # sourcery skip: extract-method
    if request.method =='POST':
            name = request.POST['recipe-name']
            desc = request.POST['recipe-description']
            img = request.FILES['recipe-image']
            new_recipe = Recipe(rname=name,rdesc=desc,rimg=img)
            new_recipe.save()
            return redirect('index')  
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request,'home.html',context)




def delete_recipe(request,id):
      delete = Recipe.objects.get(id=id)
      delete.delete()
      return redirect('/')




#MY Code
# def update_recipe(request,id):
#       if request.method =='POST':
#             name = request.POST['recipe-name']
#             desc = request.POST['recipe-description']
#             img = request.FILES['recipe-image']
#             new_recipe = Recipe(rname=name,rdesc=desc,rimg=img)
#             new_recipe.save()
#             return redirect('/')
     
      
#       update = Recipe.objects.get(id=id)
#       context = {'update':update}
#       return render(request,'update.html',context)    
 

 

def update_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == 'POST':
        recipe.rname = request.POST['recipe-name']
        recipe.rdesc = request.POST['recipe-description']
        if 'recipe-image' in request.FILES:
            recipe.rimg = request.FILES['recipe-image']
        recipe.save()
        return redirect('/')
    update = Recipe.objects.get(id=id)
    context = {'update':update}
    return render(request,'update.html',context)









def register(request):
     if request.method == 'POST':
      name = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      new_user = User.objects.create(username=name, email=email)
      new_user.set_password(password)
      new_user.save()
      return redirect('login')
     return render(request,'register.html')






def login_page(request):
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches
     if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request,username=username,password=password)
      if user is not None:
            login(request,user)
            return redirect('index')
      else : 
           return HttpResponse('Invalid Credientials')
     return render(request,'login.html')

      
      

     

              
def logout_view(request):
    logout(request)
    return HttpResponse('Logged Out Successfully')
        

