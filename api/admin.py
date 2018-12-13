from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import (
    
    DoctorProfile,
    Scheduel,
    Speciality,
    Rating,
    Area,
    City,
    UserProfile
)

class ScheduelAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'date']

class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User-Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(DoctorProfile)
admin.site.register(Scheduel, ScheduelAdmin)
admin.site.register(Speciality)
admin.site.register(Rating)
admin.site.register(Area)
admin.site.register(City)

