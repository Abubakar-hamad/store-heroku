from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.



class Brand(models.Model):
    BRNDProductName=models.CharField(max_length=50 ,  verbose_name=_("Brand name"))
    BRNDProductDis=models.TextField(max_length=100 , blank=True , null=True ,  verbose_name=_("Brand Desc"))

    class Meta:

        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return self.BRNDProductName

   


class Variant(models.Model):
   
    VarName = models.CharField(max_length=30 ,  verbose_name=_("Variant Name"))
    VarDes = models.TextField(max_length=100 , blank=True , null=True , verbose_name=_("Variant Descri"))
    
    
    
    class Meta:
        verbose_name = _('Variant')
        verbose_name_plural = _('Variants')

    def __str__(self):
        return self.VarName