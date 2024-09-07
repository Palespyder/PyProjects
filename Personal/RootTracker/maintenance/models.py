from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from buildings.models import Building  # Assuming this exists

class MaintenanceTask(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    # Link to the building
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='maintenance_tasks')

    # New fields for external maintenance providers
    provider_name = models.CharField(max_length=255, blank=True, null=True)
    provider_phone = models.CharField(max_length=15, blank=True, null=True)
    provider_email = models.CharField(max_length=255, blank=True, null=True)
    maintenance_date = models.DateField(blank=True, null=True)  # Date when maintenance was completed
    maintenance_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.title} ({'Completed' if self.completed else 'Pending'})"


class MaintenanceDocument(models.Model):
    maintenance_task = models.ForeignKey(MaintenanceTask, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to='maintenance_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document for {self.maintenance_task.title} uploaded at {self.uploaded_at}"
    
class Reminder(models.Model):
    RECURRENCE_CHOICES = [
        ('weekly', 'Once per week'),
        ('monthly', 'Once per month'),
        ('yearly', 'Once per year'),
        ('2years', 'Once per 2 years'),
        ('3years', 'Once per 3 years'),
        ('10years', 'Once per 10 years'),
    ]

    task = models.ForeignKey(MaintenanceTask, on_delete=models.CASCADE, related_name='reminders')
    recurrence = models.CharField(max_length=10, choices=RECURRENCE_CHOICES)
    last_reminded = models.DateField()  # The last time a reminder was sent
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Reminder for {self.task} - {self.get_recurrence_display()}"

    def is_due(self):
        """Check if the reminder is due based on recurrence."""
        if self.recurrence == 'weekly':
            return (timezone.now().date() - self.last_reminded).days >= 7
        elif self.recurrence == 'monthly':
            return (timezone.now().date() - self.last_reminded).days >= 30
        elif self.recurrence == 'yearly':
            return (timezone.now().date() - self.last_reminded).days >= 365
        elif self.recurrence == '2years':
            return (timezone.now().date() - self.last_reminded).days >= 730
        elif self.recurrence == '3years':
            return (timezone.now().date() - self.last_reminded).days >= 1095
        elif self.recurrence == '10years':
            return (timezone.now().date() - self.last_reminded).days >= 3650
        return False


class ReminderLog(models.Model):
    reminder = models.ForeignKey(Reminder, on_delete=models.CASCADE, related_name='logs')
    date_completed = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log for {self.reminder.task} on {self.date_completed}"
