from django.urls import path
from django.urls.conf import include
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls'))
]