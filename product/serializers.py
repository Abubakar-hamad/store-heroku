#get all data form my model


from rest_framework import  serializers
from . models import Product


class ProductSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'