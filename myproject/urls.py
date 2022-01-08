from django.contrib import admin
from django.urls import path, include
from . views import *

######################## Untuk Media ##############################
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   path('admin/', admin.site.urls),
   path('dashboard/', include('blog.urls')),
   path('users/',include('users.urls')),
   path('', home, name='home'),
   path('filter/<str:nama>',artikel_filter, name='artikel_filter'),
   path('artikel/<int:id>/detail/', detail_artikel, name='detail_artikel'),
   path('about/', about, name='about'),
   path('login/', login, name='login'),
   path('logout/', logout_view, name='logout'),
   path('register/', registrasi, name='registrasi'),
   
   path('ckeditor/', include('ckeditor_uploader.urls')),
]

########################## Untuk Media ##############################
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)