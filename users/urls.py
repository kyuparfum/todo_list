from django.urls import path, include
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('userlist/', views.UserListView.as_view(), name='user_list_view'),
    path('login/', views.LoginView.as_view(), name='login_view'),
    path('<int:user_id>/', views.UserEditView.as_view(), name='user_edit_view'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
