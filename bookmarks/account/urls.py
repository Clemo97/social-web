from django.urls import path, include
from django.contrib.auth views as auth_views
from . import views

urlpatterns = [
    # post views
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
]