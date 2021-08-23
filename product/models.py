from django.db import models
from django.conf import settings 
from datetime import datetime  
from django.utils.timezone import timezone  
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
# from slugify import slugify, Slugify, UniqueSlugify


from django.urls import reverse  
# from django.utils

# Create your models here.


class Product(models.Model):
    PRuser = models.ForeignKey(User, verbose_name=_( "user_name"), null = True,  on_delete = models.CASCADE )
    PRName = models.CharField(max_length=15 , verbose_name=_("Title") )
    PRDesc = models.TextField(verbose_name=_("Description "))
    PRCategory = models.ForeignKey('Category' ,related_name='procat' , on_delete= models.CASCADE  , verbose_name=_("Category"),blank=True , null=True)
    PRBrand = models.ForeignKey('settings.Brand' , on_delete=models.CASCADE , verbose_name=_("Brand") , blank=True , null=True )
    PRPrice = models.DecimalField(decimal_places=2 , max_digits=9 , null=True, verbose_name= _(" Price"))
    PRImage = models.ImageField(upload_to='static/site_static/images/product-detail' , blank=True , null=True , verbose_name=_("Product Image") )
    PRContact = models.IntegerField ( verbose_name=_("Conatct Number") , blank=True ,null=True)
    PRAddress = models.CharField(max_length=30 , null=True , blank=True , verbose_name=_("Address"))
    PRIsNew = models.BooleanField(default=False , verbose_name=_("New"))
    PRIsUsed = models.BooleanField(default=True , verbose_name=_("Used"))
    PRCreate = models.DateTimeField(auto_now_add=True , verbose_name=_("Created At"))
    PRSold = models.BooleanField(default=False , verbose_name=_("Sold"))
    PRSlug = models.SlugField(null=True , blank=True , allow_unicode=True)
    class Meta:
        ordering = ['-PRCreate',]



    def save(self , *args  , **kwargs):
        if not self.PRSlug :
            self.PRSlug = slugify(self.PRName)
        super(Product , self).save(*args , **kwargs)


        



    def get_absolute_url(self):
        # from django.core.urlresolvers import reverse
        return reverse('products:single_product', kwargs={'slug': self.PRSlug})

    def __str__(self):
        return self.PRName 
    

class ProductImage(models.Model):
    PRImgProduct=models.ForeignKey(Product, on_delete=models.CASCADE)
    PRImage = models.ImageField(upload_to='static/site_static/images/product-detail' , verbose_name=_("Product Images"))


    def __str__(self):
            return str(self.PRImgProduct)


class Category(models.Model):
    CAName = models.CharField(max_length=50 )
    CAParent = models.ForeignKey('self' , on_delete=models.CASCADE , blank=True, null=True)
    CAImage = models.ImageField(upload_to='category/' , blank=True , null= True)
    slug = models.SlugField(null=True ,  blank=True)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural=("Categories")

    def save(self , *args  , **kwargs):
        if not self.slug :
            self.slug = slugify(self.CAName)
        super(Category , self).save(*args , **kwargs)

    def __str__(self):
        return(self.CAName)





class ProductNative(models.Model):
    PRNName = models.ForeignKey(Product , on_delete= models.CASCADE , related_name= 'Main_Product')
    PRAlternatives= models.ManyToManyField(Product , related_name='Alternatives_Product')


    def __str__(self):
        return(self.PRNName)



