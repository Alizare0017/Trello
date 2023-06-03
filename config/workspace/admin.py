from django.contrib import admin
from .models import Membership, Workspace, Board

# Register your models here.

class WorkspaceAdmin(admin.ModelAdmin):
    model = Workspace
    list_display = ('id','display_owner','code','subject')

    def display_owner(self,obj):
        return obj.owner.id
    display_owner.short_description = 'Owner'

class MembershipAdmin(admin.ModelAdmin):
    model = Membership
    list_display = ('id','workspace','user')

class BoardAdmin(admin.ModelAdmin):
    model = Board
    list_display = ('id','workspace_id','visiblity','title')

admin.site.register(Board, BoardAdmin)
admin.site.register(Workspace, WorkspaceAdmin)
admin.site.register(Membership, MembershipAdmin)