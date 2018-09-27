from django.contrib import admin
from .models import (
    City,
    Address,
    DoctorProfile,
    Scheduel
)

admin.site.register(City)
admin.site.register(Address)
admin.site.register(DoctorProfile)
admin.site.register(Scheduel)


