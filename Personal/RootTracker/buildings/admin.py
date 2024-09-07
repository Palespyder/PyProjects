from django.contrib import admin
from .models import Building, BuildingDocument

class BuildingDocumentInline(admin.TabularInline):
    model = BuildingDocument
    extra = 1  # Number of extra document forms to display

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'size', 'constructed_date', 'building_type', 'address')
    inlines = [BuildingDocumentInline]  # Allows managing documents inline with the building
