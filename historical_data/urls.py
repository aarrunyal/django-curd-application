from django.urls import path
from . import views


urlpatterns = [
     path('', views.price_history_list, name='price_history_list'),
    path('view/<int:pk>', views.price_history_view, name='price_history_view'),
    path('new', views.price_history_create, name='price_history_form'),
    path('view/<int:pk>', views.price_history_view, name='price_history_view'),
    path('edit/<int:pk>', views.price_history_update, name='price_history_update'),
    path('delete/<int:pk>', views.price_history_delete, name='price_history_delete'),   
]
