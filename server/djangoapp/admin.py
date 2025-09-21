from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of extra blank forms

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('car_make', 'name', 'type', 'year', 'dealer_id', 'mileage')
    list_filter = ('car_make', 'type', 'year')
    search_fields = ('name',)

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)