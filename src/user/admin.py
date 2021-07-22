from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import MyUser

class MyUserAdmin(UserAdmin):
    list_display = ('nombre', 'username', 'is_admin', 'is_staff')
    search_fields = ('nombre', 'username')
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(MyUser, MyUserAdmin)