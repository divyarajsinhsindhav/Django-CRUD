from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
	path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/', views.customer, name='customer'),
    path('customerview/<str:pk_test>/', views.customer_view, name='customer_view'),

    path('createorder/', views.create_order, name='create_order'),
    path('updateorder/<str:pk>/', views.update_order, name='update_order'),
    path('removeorder/<str:pk>/', views.remove_order, name='remove_order'),

    path('user/', views.user_page, name='user_page'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]