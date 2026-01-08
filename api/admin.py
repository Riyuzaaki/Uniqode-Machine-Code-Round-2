from django.contrib import admin
from .models import Health


@admin.register(Health)
class HealthAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'status', 'timestamp', 'response_time_ms')
    list_filter = ('status', 'service_name', 'timestamp')
    search_fields = ('service_name', 'notes')
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)

