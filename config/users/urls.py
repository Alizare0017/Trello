from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("", views.UserRegisterationView.as_view(), name='user_register'),
    path("logout/", views.LogoutView.as_view(), name='logout'),
    path("<int:pk>/", views.UserRetrieveView.as_view(), name='retieve_user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]