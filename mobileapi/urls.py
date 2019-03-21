from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import rest_framework

from api import views


urlpatterns = [
	path('cafes', views.CafeView.as_view()),
	path('scheds', views.TodaySchedule.as_view()),
	path('scheds/<int:cafe_id>', views.DaySchedule.as_view()),
	path('scheds/<int:cafe_id>/<int:wd>', views.OneDaySchedule.as_view()),
	path('scheds/allcafes/<int:wd>', views.AllCafes.as_view()),
	path('menu/<int:cafe_id>', views.TodayMenu.as_view()),
	path('menu/<int:cafe_id>/<int:wd>', views.OneDayMenu.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
