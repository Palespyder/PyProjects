from django.db import models

class Building(models.Model):
    BUILDING_TYPE_CHOICES = [
        ('home', 'Home'),
        ('outbuilding', 'Outbuilding'),
    ]

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    size = models.FloatField()  # Size in square feet or another unit
    constructed_date = models.DateField()

    # New fields for building type and address
    building_type = models.CharField(max_length=15, choices=BUILDING_TYPE_CHOICES, default='home')
    address = models.CharField(max_length=255, blank=True, null=True)  # Only for home buildings

    def __str__(self):
        return self.name


class BuildingDocument(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to='building_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document for {self.building.name} uploaded at {self.uploaded_at}"
