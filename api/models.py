from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DoctorProfile(models.Model):
    # user.group_set.all().exist THIS IS FOR FRONT END CHECKING USER IS IN A GROUP
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField()
    profession = models.CharField(max_length=120)
    description = models.TextField()
    google_maps = models.URLField(max_length=450)
    waiting_time = models.DurationField()
    service = models.TextField()
    fees = models.IntegerField(blank=True, null=True)
    opening_file = models.IntegerField(blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    block = models.IntegerField()
    street = models.CharField(max_length=255)
    building = models.IntegerField(blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return (self.user.first_name + ' ' + self.user.last_name)




class Scheduel(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='doctor_schedule')
    date = models.DateField()
    time = models.TimeField()
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_schedule', null=True, blank=True)

    def __str__(self):
        return self.doctor.user.first_name
    
    def booked(self):
        return True if self.patient else False
            
    # user.doctor_schedule.all()
    # user.patient_schedule.all()
    


class FavouriteDoctor(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Rating(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField()
    # d&&&&&&&&&&&&& HOW TO LET THEM CHCOOSE BETWEEN 0 TO 5 &&&&&&&&&&&&&&



# def Offer(models.Model):
#     title = models.CharField(max_length=120)
#     description = models.TextField()
#     price = models.IntegerField()

#     def __str__(self):
#         return self.title