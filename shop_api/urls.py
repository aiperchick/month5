from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/category/', views.CategoryListAPIView.as_view()),
    path('api/v1/category/<int:id>/', views.CategoryDetailAPIView.as_view()),

    path('api/v1/product/', views.ProductListAPIView.as_view()),
    path('api/v1/product/<int:id>/', views.ProductDetailAPIView.as_view()),

    path('api/v1/reviews/', views.ReviewListAPIView.as_view()),
    path('api/v1/review/<int:id>/', views.ReviewDetailAPIView.as_view()),

    path('api/v1/products/reviews/', views.RatingAPIViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/products/reviews/<int:pk>/', views.RatingAPIViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                                              'delete': 'destroy',
                                                                              'patch': 'partial_update'})),

    path('api/v1/users/', include('users.urls')),
]
