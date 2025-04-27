from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Admin configuration for the Contact model."""
    list_display = ('name', 'email', 'short_message', 'created_at', 'was_recently_submitted')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    
    def short_message(self, obj):
        """Truncate message for display in list view."""
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    short_message.short_description = 'Message'
    
    def was_recently_submitted(self, obj):
        """Check if message was submitted in the last 24 hours."""
        from django.utils import timezone
        import datetime
        return obj.created_at >= timezone.now() - datetime.timedelta(days=1)
    was_recently_submitted.short_description = 'Recent'
    was_recently_submitted.boolean = True
