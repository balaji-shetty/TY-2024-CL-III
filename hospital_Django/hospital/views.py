from django.shortcuts import render, redirect
from .models import Department, Doctor, Patient, Appointment
from .forms import DepartmentForm, DoctorForm, PatientForm, AppointmentForm

def add_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')  # Corrected here
    else:
        form = DepartmentForm()
    return render(request, 'hospital/add_department.html', {'form': form})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'hospital/department_list.html', {'departments': departments})

def patient_list(request):
    patients = Patient.objects.all()  # Get all patients from the database
    return render(request, 'hospital/patient_list.html', {'patients': patients})

def add_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')  # Redirect after successful form submission
    else:
        form = DoctorForm()
    return render(request, 'hospital/add_doctor.html', {'form': form})

def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')  # Redirect after successful form submission
    else:
        form = PatientForm()
    return render(request, 'hospital/add_patient.html', {'form': form})

def home(request):
    return render(request, 'hospital/home.html')

def doctor_list(request):
    doctors = Doctor.objects.all()  # Get all doctors from the database
    return render(request, 'hospital/doctor_list.html', {'doctors': doctors})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request,'hospital/appointment_list.html',{'appointments':appointments})

def create_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')  # Redirect after successful form submission
    else:
        form = AppointmentForm()
    return render(request, 'hospital/create_appointment.html', {'form': form})