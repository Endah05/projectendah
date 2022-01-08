from django.urls import path, include
from . views import *


urlpatterns = [
   path('', dashboard, name='dashboard'),
   path('artikel/',artikel, name='tabel_artikel'),
   path('artikel/tambah',tambah_artikel, name='tambah_artikel'),
   path('artikel/lihat/<str:id>',lihat_artikel, name='lihat_artikel'),
   path('artikel/edit/<str:id>',edit_artikel, name='edit_artikel'),
   path('artikel/delete/<str:id>',delete_artikel, name='delete_artikel'),
   path('users',users, name='tabel_users'),

   # api
   path('api/artikel/list/<str:x_api_key>', artikel_list, name='artikel_list'),
   path('api/artikel/post/<str:x_api_key>', artikel_post, name='artikel_post'),
   path('api/artikel/detail/<int:pk>/<str:x_api_key>', artikel_detail, name=' artikel_detail'),
]
