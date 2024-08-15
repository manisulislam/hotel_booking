from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('people/',include('people.urls')),
    path('hotel/',include('hotel.urls')),
    path('transaction/',include('transaction.urls'))
]
urlpatterns += staticfiles_urlpatterns()
