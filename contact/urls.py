from django.urls import path , include

from. import views

app_name = 'contact'

urlpatterns = [
    # path('', views.home_view),
    path('contact/', views.contact_view),




]