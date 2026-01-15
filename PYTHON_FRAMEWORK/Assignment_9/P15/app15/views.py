from django.shortcuts import render
from app15.models import *

# Create your views here.

def index(request):
    specialties = Specialty.objects.all()
    doctors = []
    selected_specialty = None

    if request.method == 'POST':
        specialty_id = request.POST.get('specialty')
        if specialty_id:
            selected_specialty = Specialty.objects.get(id=specialty_id)
            doctors = Doctor.objects.filter(specialty=selected_specialty)
    else:
        doctors = Doctor.objects.all()

    context = {
        'specialties': specialties,
        'doctors': doctors,
        'selected_specialty': selected_specialty
    }
    return render(request, 'index.html', context)