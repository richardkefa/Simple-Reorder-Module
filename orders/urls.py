from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.items_lIst,name='items'),
    path('<int:id>/selling',views.sell_item,name='selling'),
    path('order_list',views.order_list,name='order_list')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)