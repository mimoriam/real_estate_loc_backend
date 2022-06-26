"""real_estate_loc_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from listings.api import views as listing_api_views
from users.api import views as users_api_views

from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/listings/', listing_api_views.ListingList.as_view()),
                  path('api/listings/<int:pk>/', listing_api_views.ListingDetail.as_view()),
                  path('api/listings/create/', listing_api_views.ListingCreate.as_view()),

                  path('api/profiles/', users_api_views.ProfileList.as_view()),
                  path('api/profiles/<int:seller>/', users_api_views.ProfileDetail.as_view()),
                  path('api/profiles/<int:seller>/update/', users_api_views.ProfileUpdate.as_view()),

                  path(r'api-auth/', include('djoser.urls')),
                  path(r'api-auth/', include('djoser.urls.authtoken')),

                  path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
                  path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs')
              ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
