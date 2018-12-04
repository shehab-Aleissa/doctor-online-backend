"""doctor_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
from api.views import (DoctorProfileList,
ScheduelList,
MakeFavourite,
ViewsCount,
FavouriteList,
RegisterAPIView,
MakeRating,
RatingList,
CityList,
SpecialityList,
UpdateView,
AreaList,
UserList,
# UserProfileCreateView,
UpdateUserProfile,
UserProfileList,
# UpdateUserProfile
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', obtain_jwt_token, name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),

    path('users/', UserList.as_view(), name='users-list'),
    path('profile/info/get&update/<int:user_id>', UpdateUserProfile.as_view(), name='user-info'),
    path('users/profiles', UserProfileList.as_view(), name='users-profiles'),
    # path('user/profile/<int:profile_id>', UpdateUserProfile.as_view(), name='user-profile'),

    path('doctor/list', DoctorProfileList.as_view(), name='doctor-list'),
    path('doctor/schedeul', ScheduelList.as_view(), name='doctor-scheduel'),

    path('make/favourite/<int:doctor_id>', MakeFavourite.as_view(), name='make-favourite'),
    path('favourite/', FavouriteList.as_view(), name='favourite'),

    path('rating/', RatingList.as_view(), name='rating'),
    path('make/rating/', MakeRating.as_view(), name='make-rating'),

    path('cities/', CityList.as_view(), name='citites'),
    path('area/', AreaList.as_view(), name='area'),

    path('speciality/', SpecialityList.as_view(), name='speciality'),
    path('doctor/views/<int:profile_id>', ViewsCount.as_view(), name='doctor-views'),
    path('update/profile/<int:profile_id>', UpdateView.as_view(), name='update-profile'),


]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
