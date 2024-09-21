from django.forms import ModelForm
from sampleApp.models import *


class RegisterForm(ModelForm):
    class Meta:
        model=ShopTable
        fields=["Name", "Shopname", "Address", "Emailid", "Phonenumber"]
class RegisterProductForm(ModelForm):
    class Meta:
        model=ProductTable
        fields=["Name", "Category", "Description","Productimages"]
class AddofferForm(ModelForm):
    class Meta:
        model=Offer
        fields=["Name","Image","Description","Offervalidity"]
        