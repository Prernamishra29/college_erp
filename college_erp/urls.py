from django.contrib import admin
from django.urls import include, path
from students import views 

urlpatterns = [
    path('admin/', admin.site.urls),  # Removed extra space
    path('', views.home, name='home'),  
    path('students/', include('students.urls')),
    path('Administrator/', include('Administrator.urls')), 
    path('faculty/', include('faculty.urls')),   
]
