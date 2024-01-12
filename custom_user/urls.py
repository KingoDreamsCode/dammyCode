from django.urls import path
from . import views
from .views import pdf_list
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', views.contact_form_view, name='index'),
  path('login/', views.login_view, name='login'),
  path('signup/', views.signup, name='signup'),
  path('shop/', views.pdf_list, name='shop'),
    path('about/', views.about, name='about'),
  path('logout/', views.logout_view, name='logout'),
  path('contact/', views.contact_form_view, name='contact'),
  path('shop/projects/<str:pk>', views.projects, name = 'projects'),
  path('sub/', views.sub, name='sub'),
  path('payment/', views.payment, name='payment'),



  path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
  path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
  path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
  path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
] 
