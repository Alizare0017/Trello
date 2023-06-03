
def has_object_permission(request, obj):
    if obj.owner_id == request.id :
        return True
    return False