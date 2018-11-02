from django.contrib import admin
from .models import (
    City,
    DoctorProfile,
    Scheduel,
    Speciality,
)

class ScheduelAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'date', '_from', 'to']

admin.site.register(City)
admin.site.register(DoctorProfile)
admin.site.register(Scheduel, ScheduelAdmin)
admin.site.register(Speciality)
