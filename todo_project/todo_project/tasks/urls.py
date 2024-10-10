from django.urls import path
from .views import Tasks, ViewTask

urlpatterns = [
    path('', Tasks.as_view(), name='task'),
    path('<int:id>/', ViewTask.as_view(), name="view-task"),
]