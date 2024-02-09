from django.urls import path
from products.views import ProductListView,ProductDetailView,CategoryListView,CategoryDetailView,FileListView,FileDetailView




urlpatterns = [
    path('categories/',CategoryListView.as_view(),name='category-list'),
    path('category/<int:pk>/',CategoryDetailView.as_view(),name='category-detail'),
    path('products/',ProductListView.as_view(),name='product-list'),
    path('product/<int:pk>/',ProductDetailView.as_view(),name='product-detail'),
    path("product/<int:product_id>/files/",FileListView.as_view(),name='file-list'),
    path("product/<int:product_id>/files/<int:pk>/",FileDetailView.as_view(),name='file-detail'),



]