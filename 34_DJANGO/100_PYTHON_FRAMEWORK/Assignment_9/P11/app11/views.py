from django.shortcuts import render, redirect
from app11.models import *
import os


# Create your views here.

def index(request):
    doctors = Doctor.objects.all()
    return render(request, 'index.html', {'doctors': doctors})

def register(request):
    if request.method == 'POST':
        doc_id = request.POST.get('id')
        name = request.POST.get('name')
        specialization = request.POST.get('specialization')
        experience = request.POST.get('experience')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        if doc_id:  # Update existing doctor
            try:
                doctor = Doctor.objects.get(pk=doc_id)
                doctor.name = name
                doctor.specialization = specialization
                doctor.experience = experience
                doctor.email = email
                doctor.contact = phone
                doctor.save()
            except Doctor.DoesNotExist:
                pass  # Optionally show error
        else:  # Create new doctor
            Doctor.objects.create(
                name=name,
                specialization=specialization,
                experience=experience,
                email=email,
                contact=phone
            )
        return redirect('index')
    return redirect('index')

def edit(request):
    did = request.GET.get('did')
    try:
        doctor = Doctor.objects.get(pk=did)
        doctors = Doctor.objects.all()
        return render(request, 'index.html', {"doctors": doctors, 'doctor': doctor})
    except Doctor.DoesNotExist:
        return redirect('index')


def delete(request):
    doid = request.GET.get('did')
    if doid:
        try:
            doctor = Doctor.objects.get(pk=doid)
            doctor.delete()
        except Doctor.DoesNotExist:
            return render(request, 'index.html', {'error': 'Doctor not found.'})
        return redirect('index')