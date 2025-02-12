from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_groups')
    search_fields = ('email', 'first_name', 'last_name', 'username',)
    read_only_fields = ('last_login', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permission', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Groups', {'fields': ('groups', 'user_permissions')}),
        ('Impotent dates', {'fields': ('last_login', 'date_joined')})
    )

    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])

    get_groups.short_description = 'Groups'
