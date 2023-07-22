from rest_framework import permissions
from rest_framework.views import Request, View


class IsUserOrEmployee(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_employee
        )


class IsUserOrAdmin(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_superuser
        )


class IsUserOnwer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_employee
            or obj == request.user
        )
    
