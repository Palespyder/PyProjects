from django.contrib import admin
from .models import MaintenanceTask, MaintenanceDocument, Reminder, ReminderLog

class MaintenanceDocumentInline(admin.TabularInline):
    model = MaintenanceDocument
    extra = 1  # Number of extra document forms to display

class ReminderLogInline(admin.TabularInline):
    model = ReminderLog
    extra = 1  # Show one empty log entry by default

@admin.register(MaintenanceTask)
class MaintenanceTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'completed', 'building', 'provider_name', 'provider_phone', 'provider_email', 'maintenance_date', 'maintenance_cost')
    inlines = [MaintenanceDocumentInline]  # Allows managing documents inline with the task

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('task', 'recurrence', 'last_reminded', 'assigned_to', 'created_at')
    list_filter = ('recurrence', 'assigned_to')
    search_fields = ('task__title', 'assigned_to__username')
    inlines = [ReminderLogInline]  # Allows adding reminder logs directly within the reminder

@admin.register(ReminderLog)
class ReminderLogAdmin(admin.ModelAdmin):
    list_display = ('reminder', 'date_completed', 'created_at')
