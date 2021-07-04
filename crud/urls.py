from django.urls import path
from .views import  *

urlpatterns = [
	path('', home, name='home'),
	path('delete/<int:id>', delete, name='delete'),
	path('update/<int:id>', update, name='update'),
	

]