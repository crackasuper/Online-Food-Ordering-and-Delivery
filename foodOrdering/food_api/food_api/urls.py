
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('food.urls')), # Include your app's URLs
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # For token auth
    path('api-auth/', include('rest_framework.urls')), # browsable API login
]

