from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ALlow user to edite their own profile"""

    def has_object_permission(self, request,view,obj):
        """Checks user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id==request.user.id

class UpdateOwnTweet(permissions.BasePermission):
    """Allows user to update their own tweet"""

    def has_object_permission(self, request,view,obj):
        """Checks user is trying to edit their own tweet"""

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.author.id==request.user.id



class UpdateOwnComment(permissions.BasePermission):
    """Allows user to update their own tweet"""

    def has_object_permission(self, request,view,obj):
        """Checks user is trying to edit their own tweet"""

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.author.id==request.user.id
