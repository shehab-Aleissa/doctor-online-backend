from rest_framework import serializers
from .models import DoctorProfile, City, Scheduel
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


class DoctorProfileSerializer(serializers.ModelSerializer):

 
    # adding the name not the id in json
    user = serializers.SerializerMethodField()
    
    city = serializers.SerializerMethodField()
    def get_user(self, obj):
        return (obj.user.first_name + ' ' + obj.user.last_name)
    
    def get_city(self, obj):
        return obj.city.name

   
    class Meta:
        model = DoctorProfile
        fields = '__all__'



class ScheduelSerializer(serializers.ModelSerializer):
    doctor = serializers.SerializerMethodField()
    
    def get_doctor(self, obj):
        return (obj.doctor.first_name + ' ' + obj.doctor.last_name)

    class Meta:
        model = Scheduel
        fields = '__all__'
