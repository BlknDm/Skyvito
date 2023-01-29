from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsSelectionOwner(BasePermission):
    message = "Это не Ваша подборка, вносить изменения может только владелец."

    def has_object_permission(self, request, view, selection):
        if request.user == selection.owner:
            return True
        return False


class IsAdOwner(BasePermission):
    message = "У Вас нет прав изменять это объявление."

    def has_object_permission(self, request, view, ad):
        if request.user == ad.author or request.user.role != UserRoles.MEMBER:
            return True
        return False