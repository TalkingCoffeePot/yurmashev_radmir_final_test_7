from django.contrib import admin
from main_app.models import GuestCard

# Register your models here.
class GuestCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mail', 'date_create', 'date_edit', 'description', 'card_status']
    list_editable = ['name', 'mail', 'description', 'card_status']


admin.site.register(GuestCard, GuestCardAdmin)