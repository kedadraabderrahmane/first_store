from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('home2',views.index_2,name='index_2'),
    path('about',views.about,name='about'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/<int:id>',views.checkout,name='checkout'),
    path('contact',views.contact,name='contact'),
    path('404',views.error,name='404'),
    path('news',views.news,name='news'),
    path('shop',views.shop,name='shop'),
    path('single-news',views.singlenews,name='single-news'),
    path('products/<int:id>',views.singleproduct,name='single-product'),
    path('decrease-cart-item/<int:product_id>/',views.decrease_cart_item,name='decrease_cart_item'),
    path('increase-cart-item/<int:product_id>/',views.increase_cart_item,name='increase_cart_item'),
    path('get-communes/', views.get_communes, name='get_communes'),
]