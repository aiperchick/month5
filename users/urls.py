from django.urls import path
from . import views

urlpatterns = [
    path('authorization/', views.AuthorizationAPIView.as_view()),
    path('registration/', views.RegistrationAipView.as_view()),
    path('api/v1/users/confirm/', views.ConfirmApiView.as_view()),
]
