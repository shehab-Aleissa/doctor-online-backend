from django.contrib import admin
from .models import (
    City,
    DoctorProfile,
    Scheduel
)

admin.site.register(City)
admin.site.register(DoctorProfile)
admin.site.register(Scheduel)


