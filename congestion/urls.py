from django.urls import include, path
'''
from congestion.views import congestion_new, congestion_save, congestion_list
'''
from rest_framework import routers
from . import views

# views.py import
'''
app_name = 'congestion'

urlpatterns = [
    path('new', congestion_new, name="new"),
    path('create', congestion_save, name="save"),
    path('index', congestion_list, name="index")
]
'''

router = routers.DefaultRouter()  # DefaultRouter를 설정
router.register('Bus', views.ItemViewSet)  # itemviewset 과 item이라는 router 등록

urlpatterns = [
    path('', include(router.urls)),
    path('get_weather/', views.get_weather_data, name='get_weather_data'),
]
