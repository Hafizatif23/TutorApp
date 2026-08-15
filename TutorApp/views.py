from django.shortcuts import render, redirect, get_object_or_404
from .models import Tutor, Booking
from django.contrib import messages

# Create your views here.
def tutor_list(request):

    tutors = Tutor.objects.all()
    return render(request, 'TutorApp/home.html', {'tutors':tutors})


def tutor_detail(request, pk):

    tutor = get_object_or_404(Tutor, id= pk)

    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        date = request.POST.get('date')
        message = request.POST.get('message')

        if not name or not contact or not date:
            return redirect('tutor_detail', pk = tutor.id)
            
        Booking.objects.create(
            tutor = tutor,
            student_name = name, 
            contact_number = contact, 
            email = email,
            date = date,
            message = message
        )

        messages.success(request, f"Your booking request with {tutor.name} was submitted successfully! The admin will review it soon.")

        return redirect('home')
    return render(request, 'TutorApp/tutor_detail.html' , {'tutor':tutor})
