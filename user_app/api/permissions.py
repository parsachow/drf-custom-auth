from rest_framework import permissions

class CustomUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #check permissions for get only req
        if request.method in permissions.SAFE_METHODS:
            #safe_methods = GET req and will return- True, if we want to grant permission for user to read object
            return True
        else:
            return obj.user == request.user #checking to see if the person who is currently accessing the user info is the logged in user themselves