#work like views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


from . models import Product
from . serializers import ProductSerilizers

@api_view(['GET'])

def products_api(request):
    product_api = Product.objects.all()
    data = ProductSerilizers(product_api , many=True).data
    return Response({'data':data})

@api_view(['GET'])
def product_detail_api(request , pk):
    product_detail_api = Product.objects.get(id=pk)
    data = ProductSerilizers(product_detail_api).data
    return Response({'data':data})


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerilizers
    queryset = Product.objects.all()
    lookup_fields = ['id']

class ListVCreat(generics.ListCreateAPIView):
    serializer_class = ProductSerilizers
    queryset = Product.objects.all()


    
    