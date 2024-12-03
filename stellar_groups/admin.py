from django.contrib import admin
from . import models

class StellarGroupMemberInline(admin.TabularInline):
    model = models.StellarGroupMember  

@admin.register(models.StellarGroup)
class StellarGroupAdmin(admin.ModelAdmin):
    inlines = [StellarGroupMemberInline]
