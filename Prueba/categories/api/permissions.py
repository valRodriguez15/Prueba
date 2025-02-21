from rest_framework.permissions import BasePermission
#Solo los usuarios que sean staff pueden editar datos en el CMS
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        else:
            return  request.user.is_staff
