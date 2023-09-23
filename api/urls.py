from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'api'

router = SimpleRouter()
router.register('lessons', views.LessonViewSet)
router.register('products', views.ProductViewSet)
router.register('timeinfo', views.TimeInfoViewSet)
router.register('students', views.StudentViewSet)

urlpatterns = [
    path('list/<pk>/', views.CurrentProductViewSet.as_view({'get': 'list'})),
    path('list/', views.ListViewSet.as_view({'get': 'list'})),
    path('', include(router.urls)),
]
