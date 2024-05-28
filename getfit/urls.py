from django.contrib import admin
from django.urls import include, path
from mainpages.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('getfit/', include('mainpages.urls')),
]
