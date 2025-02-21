from rest_framework.routers import DefaultRouter
from categories.api.views import CategoryActsApiView,CategoryToursApiView

router_categories = DefaultRouter()

router_categories.register(prefix='tours', basename='tours', viewset=CategoryToursApiView)
router_categories.register(prefix='activities', basename='activities', viewset=CategoryActsApiView)
