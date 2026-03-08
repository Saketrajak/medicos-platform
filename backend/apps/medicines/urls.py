from django.urls import path
from .views import get_medicines, get_medicine_detail, get_categories


urlpatterns = [

    path("medicines/", get_medicines),

    path("medicines/<int:id>/", get_medicine_detail),

    path("categories/", get_categories),
]