# 5. urls.py
from django.urls import path
from .views import restaurant_list, restaurant_detail
from .import views

urlpatterns = [
    path('', restaurant_list, name='restaurant_list'),
    path('restaurant/<int:restaurant_id>/', restaurant_detail, name='restaurant_detail'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('leave_review/<int:restaurant_id>/', views.leave_review, name='leave_review'),
    path('search/', views.search_view, name='search'),
]
