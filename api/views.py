from django.shortcuts import render
from .serializers import (DoctorProfileSerializer,
ScheduelSerializer,
GetFavouriteDoctorSerializer,
RegisterSerializer,
PostFavouriteDoctorSerializer,
GetRatingSerializer,
PostRatingSerializer,
CitySerializer,
SpecialitySerializer,
AreaSerializer)

from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView, CreateAPIView
) 
from rest_framework import status
from rest_framework.views import APIView
from .models import DoctorProfile, Scheduel, FavouriteDoctor, Rating, City, Speciality, Area
# Create your views here.

#REGISTERING
class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer


class DoctorProfileList(ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer

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

class CityList(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class AreaList(ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    
class SpecialityList(ListAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer