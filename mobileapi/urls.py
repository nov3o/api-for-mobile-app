from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import rest_framework

from api.views import TodayMenu, OneDayMenu
from cafeterias.views import CafeView
from schedules.views import (CafeTodaySchedule,
	OneDayCafeSchedule, AllTodaySchedules)


urlpatterns = [
	path('cafes', CafeView.as_view()),
	path('scheds', AllTodaySchedules.as_view()),
	path('scheds/<int:cafe_id>', CafeTodaySchedule.as_view()),
	path('scheds/<int:cafe_id>/<int:wd>', OneDayCafeSchedule.as_view()),
	path('menu/<int:cafe_id>', TodayMenu.as_view()),
	path('menu/<int:cafe_id>/<int:wd>', OneDayMenu.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
