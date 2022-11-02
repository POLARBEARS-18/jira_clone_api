from rest_framework import permissions


class OwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # save method以外でのメソッドの場合で、ownerIdとrequestIdが一致していればtrueを返す
        return obj.owner.id == request.user.id

