
from django.shortcuts import render , get_object_or_404 , redirect
from . models import  Product , Category 
from django.core.paginator import Paginator
from django.template import loader
import random
from django.views.generic import (CreateView , ListView , UpdateView)

from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from .filters import  ProductFilter  
from . forms import AddProductForm 

# from accounts.models import Profile

# from django.http import HttpResponse



def home_view(request  ):
    # categoreis=Category.objects.all()
    letest_product = list(Product.objects.all().order_by('-PRCreate',))[0:10]
    
    
    context={'letest_product':letest_product 
    # ,  'categoreis':categoreis

    }
    return render(request, "base.html" , context  )





def all_product(request ):
    # return HttpResponse("<h1>hi</h1>")
    all_product = Product.objects.all()

    filter_data = ProductFilter(request.GET , queryset=all_product)
    all_product = filter_data.qs

    ordering =['-PRCreate']


    paginator = Paginator(all_product, 8) # Show 25 contacts per page.

    page = request.GET.get('page')
    all_product = paginator.get_page(page)
    context = {'all_product' : all_product , 
    'filter_data':filter_data , 
    'ordering':ordering
    }
    return render (request , 'Product/all_product.html'  , context )




def single_product (request  , slug ,*args, **kwargs ):
#  search box "not working yet"

    all_product = Product.objects.all()   
    search_data = ProductFilter(request.GET , queryset=all_product)
    all_product = ProductFilter.qs
    


    single_product = Product.objects.get(PRSlug = slug)


# random producct
    related_product = list(Product.objects.all())
    related_product = random.sample(related_product , 5)


#  recent product
    recent_product = list(Product.objects.all().order_by('-PRCreate')) [0:5]
    # recent =(recent_product , 5)

#  random product
    prod = list (Product.objects.all())
    prod = random.sample(prod , 5)
   

# reviews 
    # if request.method == 'POST' and request.user.is_authenticated:
    #     stars= request.POST.get('stars' ,3)
    #     content = request.POST.get('content' , '')
    #     review = ProductReview.objects.create(product = product , user = request.user , stars=stars , content=content)
    #     return redirect('single_product', category_slug=category_slug, slug=slug)
    context = {
        'all_product':all_product ,
        'search_data':search_data,
        'single_product' : single_product ,
     
        'related_product':related_product , 
        'recent_product':recent_product , 
        'prod'  : prod ,
         }
    return render (request , 'Product/single_product.html' , context)


@login_required
def product_form( request):
    post_data =request.POST or None
    file_data=request.FILES or None
    letest_product = Product.objects.all().order_by('-PRCreate',)

    add_product = AddProductForm(post_data , file_data )
    if add_product.is_valid():
       
        add_product.save()
        return redirect('/products/')
    

    context = {'add_product':add_product , 'letest_product':letest_product }
    return render(request , 'Product/add_product.html' , context  )



def my_product(listView  ):
    queryset = Product.objects.all()
    context={'queryset':queryset}
    

    return render(listView , 'Product/my_product.html' , context  )



def UpdateProduct(request , pk):
    quryset= Product.objects.get(id=pk)
    form=AddProductForm(instance=quryset)
    if request.method == 'POST':
        form = AddProductForm(request.POST , instance=quryset)
        if form.is_valid:
            form.save()
            return redirect('/my_product')
    context = {
        'form':form , 
        'quryset':quryset
    }
    return render (request ,'Product/edit_product.html' , context )

def DeleteProduct(request , pk ):
    quryset= Product.objects.get(id=pk)
    if request.method == 'POST':
        quryset.delete()
        return redirect('/my_product')
    return render(request , 'Product/delete_product.html')
