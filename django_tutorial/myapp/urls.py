from django.urls import path, include
from .views import room, room_with_id

urlpatterns = [
    path('', room),
    path('<int:id>/', room_with_id),
]
