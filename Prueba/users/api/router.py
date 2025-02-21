from django.urls import path
from users.api.views import RegisterView, UserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('auth/register', RegisterView.as_view()),
    #Devuelve el login del access token
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #Devuelve el refresh token
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/me', UserView.as_view())
]
