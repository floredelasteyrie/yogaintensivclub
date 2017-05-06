from django.contrib import admin
from .models import Activity, Sport


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('sport', 'user', 'durée', 'date', 'newsport')
    list_filter = ('user', 'sport')
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('user', 'sport', 'date', 'durée')

admin.site.register(Activity, ActivityAdmin)

class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories_coeff')
    list_filter = ('name', 'calories_coeff')
    ordering = ('name', )
    search_fields = ('name', 'calories_coeff')

admin.site.register(Sport, SportAdmin)
