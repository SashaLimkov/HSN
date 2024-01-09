from django.contrib import admin
from .models import *

class OrganInline(admin.TabularInline):
    model = Organ.systems.through
    extra = 0

class SystemAdmin(admin.ModelAdmin):
    inlines = [OrganInline, ]


# Register your models here.
admin.site.register(System, SystemAdmin)
admin.site.register(Organ)
admin.site.register(Parametr)
admin.site.register(Research)
admin.site.register(Conclusion)