import django_filters
from django.utils.translation import ugettext_lazy as _


from .models import Product



class ProductFilter(django_filters.FilterSet):
    # PRDesc = django_filters.CharFilter(lookup_expr=_('icontains'))
    PRName = django_filters.CharFilter(lookup_expr=_('icontains'))

    class Meta:
        model = Product
        fields = ['PRName' , 'PRCategory' ]
  

# class Search(django_filters.FilterSet):
    

#     class Meta:
#         model= Product
#         fields = ['PRName' , 'PRCategory' ]
#         PRName = django_filters.CharFilter(lookup_expr=_('icontains'))