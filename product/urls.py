
from django.urls import path , include
from . import api

from. import views

app_name = 'product'


urlpatterns = [
    path('', views.home_view),
    path('products/' ,views.all_product) , 
    path('add_product/' , views.product_form) ,

    path('my_product',views.my_product, name='my_product'),


    
    
    path('my_product/delete_product/<str:pk>' , views.DeleteProduct , name='delete'),
    path('my_product/edit_product/<str:pk>' , views.UpdateProduct , name='update'),
    path('<slug:slug>' , views.single_product , name='single_product'), 

    ##api
    path('api/products' , api.products_api  , name='productsapi') ,
    path('api/products/<str:pk>' , api.product_detail_api  , name='productdetailapi') ,

  ##api v2
    path('api/v2/products/<str:pk>' , api.ProductDetail.as_view()  , name='ProductDetailApi') ,
    path('api/v2/products' , api.ListVCreat.as_view()  , name='ListVCreat') ,
    

   


]