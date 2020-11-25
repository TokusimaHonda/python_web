from django.contrib import admin
from django.urls import path,include
from .views import helloworldfunction,HelloWorldClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', helloworldfunction),
    path('helloworld2/', HelloWorldClass.as_view()),
    path('apple/', include('helloworldapp.urls')),
]
