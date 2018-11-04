from rest_framework import serializers
from .models import DoctorProfile, City, Scheduel, FavouriteDoctor, Rating, Speciality, Area
from django.contrib.auth.models import User


class LogingInSerializer(serializers.ModelSerializer):
    the_username = serializers.CharField(max_length=120)
    the_password = serializers.CharField(write_only=True)



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'token', ]

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)

        validated_data["token"] = token
        return validated_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]




class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"



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

   

class GetFavouriteDoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    doctor_name = serializers.SerializerMethodField()

    class Meta:
        model = FavouriteDoctor
        fields = ['user', 'doctor_name']

    def get_doctor_name(self, obj):
        return obj.doctor.user.get_full_name()

    
class PostFavouriteDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteDoctor
        fields = "__all__"



class GetRatingSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    doctor = serializers.SerializerMethodField()

    class Meta:
        model = Rating
        fields = ['user', 'doctor', 'ratings']

    def get_doctor(self, obj):
        return obj.doctor.user.get_full_name()



class PostRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"

class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = "__all__"
