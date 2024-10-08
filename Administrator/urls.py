from django.urls import path
from . import views

app_name = 'administrator'

urlpatterns = [
     path('Administrator/', views.admin_view, name='admin_view'),
    path('manage-faculty/', views.manage_faculty, name='manage_faculty'),
    path('add-faculty/', views.add_faculty, name='add_faculty'),
    path('update-faculty/<int:faculty_id>/', views.update_faculty, name='update_faculty'),
    path('delete-faculty/<int:faculty_id>/', views.delete_faculty, name='delete_faculty'),
    path('manage-students/', views.manage_students, name='manage_students'),
    path('add-student/', views.add_student, name='add_student'),
    path('update-student/<int:student_id>/', views.update_student, name='update_student'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
]
