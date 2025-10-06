from django.contrib import admin
from website.models import Contact
# Register your models here.
class contactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'email', 'subject', 'created_date')
    ordering = ['-created_date']
    list_filter = ('email',)
    search_fields = ['name', 'email']

admin.site.register(Contact, contactAdmin)