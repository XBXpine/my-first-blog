from django.urls import re_path as url
from django.contrib import admin
from polls import views
from django.urls import include, path

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]