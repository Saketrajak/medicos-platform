from django.urls import path
from .views import create_order, order_history, order_detail

urlpatterns = [

    path("create/", create_order),

    path("history/", order_history),

    path("<int:id>/", order_detail),

]