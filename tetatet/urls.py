from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wishes.urls')),
    path('api/articles/', include('articles.urls')),
    path('api/auth/', include('authentication.urls')),
]
