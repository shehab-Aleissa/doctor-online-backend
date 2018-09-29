from rest_framework import serializers
from .models import DoctorProfile, City, Scheduel, FavouriteDoctor
from django.contrib.auth.models import User


class LogingInSerializer(serializers.ModelSerializer):
    the_username = serializers.CharField(max_length=120)
    the_password = serializers.CharField(write_only=True)



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]




class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'




class ScheduelSerializer(serializers.ModelSerializer):
    booked = serializers.SerializerMethodField()
    patient = UserSerializer()

    class Meta:
        model = Scheduel
        fields = '__all__'

    def get_booked(self, obj):
        return obj.booked()



class DoctorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    city = CitySerializer()
    schedule = serializers.SerializerMethodField()
    
    class Meta:
        model = DoctorProfile
        fields = '__all__'

    def get_schedule(self, obj):
        schedule = obj.doctor_schedule.all()
        return ScheduelSerializer(schedule, many=True).data

   

class FavouriteDoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # doctor = DoctorProfileSerializer()
    doctor_name = serializers.SerializerMethodField()

    class Meta:
        model = FavouriteDoctor
        fields = ['user', 'doctor_name']

    def get_doctor_name(self, obj):
        return obj.doctor.user.get_full_name()

        



