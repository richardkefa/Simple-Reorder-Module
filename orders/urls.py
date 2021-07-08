# from .views import send_order,sell_item,items_lIst
from django.urls import path
from . import views

urlpatterns = [
    path('',views.items_lIst,name='items'),
    path('<int:id>/selling',views.sell_item,name='selling'),
    path('<int:id>/sending_order',views.send_order,name='sending_order')
]