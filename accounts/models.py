from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify 

import datetime
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User , verbose_name=_("user") , on_delete= models.CASCADE)
    image = models.ImageField(upload_to = 'static/site_static/images/profile-images' , verbose_name=_("Image") , null=True , blank=True)
    phone_number= models.CharField(verbose_name=_("phone") , max_length=15,blank=True, null=True)
    country = CountryField()
    address = models.CharField(max_length=100 ,verbose_name=_("address"))
    join_date = models.DateTimeField (verbose_name=_("Join Date") ,default= datetime.datetime.now)


    slug = models.SlugField(null=True , blank=True)



    # def save(self , *args , **kwargs):
    #     if not self.slug :
    #         self.slug = slugify(self.user.username)
    #     super(Profile , self).save(*args , **kwargs)
    
    
    
    
    
    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return ' %s' %(self.user)


    def get_absolute_url(self):
        return reversed ('accounts:profile' , kwargs= {'slug' :self.slug})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)




class Blacklist(models.Model):
    BLSTUser = models.CharField(max_length=50 , verbose_name=_('Name'))
    BLSTPhone = models.IntegerField(verbose_name=_('phone'))
    BLSTAddress = models.CharField(max_length=50 ,verbose_name=_('Address') , null=True)


    def __str__(self):
        return (self.BLSTUser)
