from django.contrib import admin

# Register your models here.

from . import models


@admin.register(models.Bike)
class bike(admin.ModelAdmin):
    list_display = ('BikeId','CompanyName',)

@admin.register(models.CyclingRecords)
class cyclingRecords(admin.ModelAdmin):
    list_display = ('id','BikeId','UserId',)

@admin.register(models.RepairRecords)
class repairRecords(admin.ModelAdmin):
    list_display = ('id','BikeId','CenterId','RepairParts',)

@admin.register(models.Center)
class center(admin.ModelAdmin):
    list_display = ('CenterId','Location')