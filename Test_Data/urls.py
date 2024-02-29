from django.contrib import admin
from django.urls import path, include
from api import views as main_views
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('', main_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/', include('api.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
