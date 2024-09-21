from django.urls import path
from sampleApp.views import *

urlpatterns = [
    path('', homepage.as_view(), name="homepage"),
    path('loginpage/', loginpage.as_view(), name="loginpage"),
    path('adminDashboard/', adminDashboard.as_view(), name="adminDashboard"),
    path('reply/', reply.as_view(), name="reply"),
    path('shop/', shop.as_view(), name="shop"),
    path('addoffer/', Addoffer.as_view(), name="addoffer"),
    path('addproduct/',Addproduct.as_view(),name='Addproduct')

]
