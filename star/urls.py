from . import views
from django.urls import path
app_name = 'star'
urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new_post, name='new_post'),
    path('graf/', views.graf, name='graf'),

]