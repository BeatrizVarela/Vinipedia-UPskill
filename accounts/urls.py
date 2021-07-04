import django.contrib.auth.views as auth_views
from django.urls import path
from . import views
from .views import ProfilesList

app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='homepage'), name='logout'),
    path('register/', views.register, name='register'),
    path('edit/<int:profile_id>', views.edit, name='edit'),
    path('profile/<int:user_id>', views.profile, name='profile'),

    path('profiles/', ProfilesList.as_view(), name='profile_list'),
    path('visit_profile/<int:profile_id>', views.visit_profile, name='visit_profile'),
    path('delete_profile/<int:profile_id>', views.delete_profile, name='delete_profile')
]
