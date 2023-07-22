from rest_framework import permissions
from rest_framework.views import Request, View
from movies.models import Movie


class IsMovieOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        return obj == request.user
