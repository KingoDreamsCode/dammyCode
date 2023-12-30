from django.urls import path
from . import views
from .views import pdf_list

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('shop/', views.pdf_list, name='shop'),
  path('logout/', views.logout_view, name='logout'),
] 
