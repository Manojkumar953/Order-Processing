from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrdersView.as_view(), name = "view orders"),
    path('add', views.OrdersView.as_view(), name = "add order"),
    path('metrics', views.MetricsView.as_view(), name = "metrics"),
]