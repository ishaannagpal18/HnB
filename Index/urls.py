from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('blog',views.blog,name='blog'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('portfolio-single',views.portfolio_single,name='portfolio_single'),
    path('shop',views.shop,name='shop'),
    path('product-detail',views.product_detail,name='product_detail'),

]