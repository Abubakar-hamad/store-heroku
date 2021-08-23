
from django.shortcuts import render , get_object_or_404 , redirect
from django.core.mail import send_mail
from  django.conf import settings

# Create your views here.


def contact_view(request):
    if request.method =='POST':
        # name = request.POST['name']
        subject = request.POST['subject']
       
        email = request.POST['email']
        message =  request.POST['message']

        send_mail(
            subject,
            message, 
            settings.EMAIL_HOST_USER ,
            [email],
             )

    # context = {
    #     'name':name , 
    #     'email':email , 
    #     'subject':subject, 
    #     'message':message
    # }
    return render(request , "contact.html" ) #context)