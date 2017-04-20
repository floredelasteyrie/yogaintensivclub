from django.contrib import admin
from .models import Activity

class ActivityAdmin(admin.ModelAdmin):
   list_display   = ('sport', 'user', 'durée', 'date')
   list_filter    = ('user','sport',)
   date_hierarchy = 'date'
   ordering       = ('date', )
   search_fields  = ('user', 'sport')


admin.site.register(Activity,ActivityAdmin)