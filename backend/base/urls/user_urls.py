from django.urls import path
from base.views import user_view as views


urlpatterns = [
 path('login',views.MyTokenObtainPairView.as_view(), name='token_obtain_pair' ),
    path('profile', views.getUserProfile, name="users-profile"),
    path('', views.getUsers, name="users"),
    path('register', views.registerUser, name="register"),
]