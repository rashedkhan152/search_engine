from django.contrib import admin
from django.urls import path, include
from searchapp.views import ajax_posting

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('searchapp.urls')),
    path('ajax-posting/', ajax_posting, name='ajax_posting')

]
