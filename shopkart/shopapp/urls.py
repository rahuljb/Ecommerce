from django.urls import path
from . import views

app_name = 'shopapp'

urlpatterns = [
    path('', views.AllProductCat, name="allprocat"),
    path('<slug:c_slug>/', views.AllProductCat, name="product_by_category"),
    path('<slug:c_slug>/<slug:p_slug>/', views.proDetail, name="productdetail"),
]
