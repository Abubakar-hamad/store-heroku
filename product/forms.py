from django import forms
from . models import Product 



class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields= '__all__'
        
        exclude = ['PRSlug' , 'PRCreate' ,   
        
        ]
        widgets = {
            'PRuser':forms.TextInput(attrs={'class':'form-control' , ' placeholder':'id' , 'id':'alkory' , 'type':'hidden'}),
        }
 
        
 

