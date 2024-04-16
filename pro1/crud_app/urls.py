from django.urls import path
from .views import *

urlpatterns = [
    path('', PanCreate.as_view()),
    path("list/", PanList.as_view()),
    path("detail/<pk>/", PanDetail.as_view()),
    path("update/<pk>/", PanUpdate.as_view()),
    path("delete/<pk>/", PanDelete.as_view()),

]
