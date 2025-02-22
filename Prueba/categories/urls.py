from django.urls import path
from .views import (
    categories_view, create_tour, edit_tour, delete_tour,
    create_activity, edit_activity, delete_activity
)

urlpatterns = [
    path('', categories_view, name="categories"),
    path('create_tour/', create_tour, name="create_tour"),
    path('delete_tour/<int:tour_id>/', delete_tour, name="delete_tour"),
    path('create_activity/', create_activity, name="create_activity"),
    path('edit_tour/<int:tour_id>/', edit_tour, name="edit_tour"),
    path('edit_activity/<int:activity_id>/', edit_activity, name="edit_activity"),
    path('delete_activity/<int:activity_id>/', delete_activity, name="delete_activity"),
]
