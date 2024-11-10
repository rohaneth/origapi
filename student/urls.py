from django.urls import path
from .views import CountryAPIView,StudentAPIView,CityAPIView,CompanyAPIView

urlpatterns = [
    path('country/', CountryAPIView.as_view(), name='country'),
    path('student/', StudentAPIView.as_view(), name='student'),
    path('city/', CityAPIView.as_view(), name='city'),
    path('company/', CompanyAPIView.as_view(), name='company'),
]