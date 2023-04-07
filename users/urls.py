from django.urls import path
from . import views

urlpatterns = [
    path('authorization/', views.AuthorizationAPIView.as_view()),
    path('registration/', views.registration_api_view),
    path('api/v1/users/confirm/', views.confirm_user_views),
]
