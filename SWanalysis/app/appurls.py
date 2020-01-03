from django.urls import path
from .  import views

urlpatterns = [
    
    path('planets/',views.planets,name='planets'),
    path('titles/',views.titles,name='titles'),
    path('planets/search/',views.search,name='search'),
    
    

]