from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('additems',views.additems,name='additems'),
    path('delete/<int:sno>/',views.delete_data,name='deletedata'),
    path('<int:sno>/',views.update_data,name="updatedata"),
    path('highstock',views.highstock,name='highstock'),
    path('lowstock',views.lowstock,name='lowstock'),
    path('publisher',views.publisher,name="publisher"),
    path('search',views.search,name="search"),
]