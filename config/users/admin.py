from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id','username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)