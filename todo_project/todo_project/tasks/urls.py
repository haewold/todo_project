from django.urls import path
from . import views
from .views import ViewTask, FilterTask

urlpatterns = [
    path('<int:id>/', ViewTask.as_view()),
    path('', FilterTask)
]