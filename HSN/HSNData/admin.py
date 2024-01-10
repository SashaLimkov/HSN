from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin

class MyAdminSite(AdminSite):
    def get_app_list(self, request):
        app_dict = self._build_app_dict(request)
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
        return app_list


class OrganInline(admin.TabularInline):
    model = Organ.systems.through
    extra = 0

class SystemAdmin(admin.ModelAdmin):
    inlines = [OrganInline, ]


admin.site = MyAdminSite()
# Register your models here.
admin.site.register(System, SystemAdmin)
admin.site.register(Organ)
admin.site.register(Research)
admin.site.register(Parametr)
admin.site.register(Conclusion)
admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)