from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'api/cafes', views.CafeView)

urlpatterns = [
	path('', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
