from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("", views.BookingViewSet, basename="booking")

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.MenuItemsView.as_view(), name="menu-list"),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view(), name="menu-detail"),
    path("booking/", include(router.urls)),
]
