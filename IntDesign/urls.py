from django.urls import path

from . import views

app_name = 'IntDesign'
urlpatterns = [
    path('', views.index, name='index'),

    path('about/', views.about, name='about'),

    path('gallery/', views.gallery, name='gallery'),

    path('service/', views.service, name='services'),

    path('order/create/', views.order_create, name='order_create'),

    path('order/list/', views.order_list, name='order_list'),

    path('order/<int:pk>/edit/', views.order_edit, name='order_edit'),

    path('order/<int:pk>/delete/', views.order_delete, name='order_delete'),

    path('blog/', views.blog, name='blog'),
]