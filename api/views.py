from django.shortcuts import render
from .serializers import (DoctorProfileSerializer,
ScheduelSerializer,
GetFavouriteDoctorSerializer,
RegisterSerializer,
PostFavouriteDoctorSerializer,
GetRatingSerializer,
PostRatingSerializer,
SpecialitySerializer,
CitySerializer,
AreaSerializer,
UserSerializer,
UpdateUserProfileSerializer,
# UpdateProfileSerializer,
UpdateDoctorProfileSerializer,
UserProfileSerializer)
from django.contrib.auth import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView
)

from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from .models import DoctorProfile, Scheduel, FavouriteDoctor, Rating, Speciality, Area, City, UserProfile
# Create your views here.

#REGISTERING
class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer


class DoctorProfileList(ListAPIView):
    queryset = DoctorProfile.objects.filter(is_doctor= True)
    serializer_class = DoctorProfileSerializer

class UserProfileCreateView(APIView):

    def post(self,request):
        
        phone_number = request.data["phone_number"]
       
        # pic = request.FILES["pic"]
        profile = UserProfile(phone_number=phone_number)
        profile.save()

        user = User.objects.get(id=user.id)
        serializer = UserProfileSerializer(user, context={'request':request})
        return Response(serializer.data)

class UpdateView(RetrieveUpdateAPIView):
    queryset = DoctorProfile.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UpdateDoctorProfileSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'


class UpdateUserProfile(RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UpdateUserProfileSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'user_id'


class ViewsCount(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, profile_id, format=None):
        doctor = DoctorProfile.objects.get(id=profile_id)
        doctor.viewers += 1
        doctor.save()
        return Response(doctor.viewers)




class ScheduelList(ListAPIView):
    queryset = Scheduel.objects.all()
    serializer_class = ScheduelSerializer

class MakeFavourite(CreateAPIView):
    queryset = FavouriteDoctor.objects.all()
    serializer_class = PostFavouriteDoctorSerializer

class MakeFavourite(APIView):
    def get(self, request, doctor_id,*args, **kwargs):
        doctor = DoctorProfile.objects.get(id=doctor_id)
        fav, created = FavouriteDoctor.objects.get_or_create(doctor=doctor, user=request.user)

        if created:
            return Response(status=status.HTTP_201_CREATED)
        else:
            fav.delete()
            return Response(status=status.HTTP_200_OK)

# THIS WILL GET ONLY THE LIST OF THE DOCTORS THAT HAVE BEEN FAVOURITE BY THE LOGGED IN USER
class FavouriteList(ListAPIView):
    serializer_class = GetFavouriteDoctorSerializer

    def get_queryset(self):
        queryset = FavouriteDoctor.objects.filter(user=self.request.user)
        return queryset

class MakeRating(CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = PostRatingSerializer


# THIS WILL GET ONLY THE LIST OF THE DOCTORS THAT HAVE BEEN RATED BY THE LOGGED IN USER
class RatingList(ListAPIView):
    serializer_class = GetRatingSerializer

    def get_queryset(self):
        queryset = Rating.objects.filter(user= self.request.user)
        return queryset

class CityList(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    


class AreaList(ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    my_words = Area.objects.order_by('name')


class SpecialityList(ListAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileList(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer