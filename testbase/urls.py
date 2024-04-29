from django.urls import path
from testbase.apps import TestbaseConfig
from testbase.views import home


app_name = TestbaseConfig.name

urlpatterns = [
    
    path('', home, name='home'),
    
]