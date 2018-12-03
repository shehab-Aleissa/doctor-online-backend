from rest_framework import serializers
from .models import DoctorProfile, Scheduel, FavouriteDoctor, Rating, Speciality, Area, City, UserProfile
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings

class LogingInSerializer(serializers.ModelSerializer):
    the_username = serializers.CharField(max_length=120)
    the_password = serializers.CharField(write_only=True)



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)
    phone_number = serializers.IntegerField()
    class Meta:
        model = User
        fields = ['username', 'password', 'token', 'email', 'first_name', 'last_name', 'phone_number']
        # fields = '__all__'

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        new_user = User(username=username, email=email, first_name=first_name, last_name=last_name,)
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
        # fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = '__all__'

class UpdateUserProfileSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer
    class Meta:
        model = UserProfile
        fields = '__all__'
        # exclude = ('username',)
 
        

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

class PostRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"

class DoctorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    area = AreaSerializer()
    schedule = serializers.SerializerMethodField()
    rating_set = PostRatingSerializer(many=True)

    class Meta:
        model = DoctorProfile
        fields = '__all__'

    def get_schedule(self, obj):
        schedule = obj.doctor_schedule.all()
        return ScheduelSerializer(schedule, many=True).data

class UpdateDoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        exclude = ('img', "viewers", "profession", "is_doctor", "user", "speciality", "area")

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



class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = "__all__"
