from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from user import views

router = DefaultRouter()
app_name = 'user'

urlpatterns = [
    path('', include(router.urls)),
    # ----------------------------- token  -------------------------------------#
    path('accounts/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # ----------------------------- refresh token -------------------------------------#
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # ----------------------------- login - otp -----------------------------------#
    path('login/', CustomLoginView.as_view(), name='log_in'),

]