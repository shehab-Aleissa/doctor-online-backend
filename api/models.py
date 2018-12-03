from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class City(models.Model):
    name = models.CharField(max_length=255, unique=True, default='city')


    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=255, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


    def __str__(self):
        return self.name



class Speciality(models.Model):
    name = models.CharField(max_length=120)
    img = models.ImageField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=True)
    


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class DoctorProfile(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    img = models.ImageField()
    viewers = models.PositiveIntegerField(default=0)
    profession = models.CharField(max_length=120)
    description = models.TextField()
    google_maps = models.URLField(max_length=450)
    waiting_time = models.DurationField()
    service = models.TextField()
    fees = models.IntegerField(blank=True, null=True)
    opening_file = models.IntegerField(blank=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    block = models.IntegerField()
    street = models.CharField(max_length=255)
    building = models.IntegerField(blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    is_doctor = models.BooleanField(default=False)

    def __str__(self):
        return (self.user.first_name + ' ' + self.user.last_name)




class Scheduel(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='doctor_schedule')
    date = models.DateField()
    _from = models.TimeField()
    to = models.TimeField()
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
    RATING_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
    )

    ratings = models.IntegerField(choices=RATING_CHOICES, default=1)



# def Offer(models.Model):
#     title = models.CharField(max_length=120)
#     description = models.TextField()
#     price = models.IntegerField()

#     def __str__(self):
#         return self.title
