from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get/', views.getInfo,  name='getinfo'),
    path('post/', views.postInfo, name='postinfo'),
    path('redirect/', views.toRedirect,  name='redirect'),
    path('basket/', views.toGetBasket,  name='getBasket'),
    path('basket/goods/<int:object_id>', views.toGetItemById,  name='getItem')
]