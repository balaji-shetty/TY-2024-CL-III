from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('patients/', views.patient_list, name='patient_list'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('add-doctor/', views.add_doctor, name='add_doctor'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('create-appointment/', views.create_appointment, name='create_appointment'),
    path('add-department/', views.add_department, name='add_department'),
    path('department-list/', views.department_list, name='department_list'),
    # path('Student_list/', views.student_list, name='student_list'),
]

