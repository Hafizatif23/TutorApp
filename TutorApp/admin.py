from django.contrib import admin
from .models import Tutor, Booking
from django.core.mail import send_mail
# Register your models here.

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'bio')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('student_name', 'contact_number', 'tutor', 'status', 'date', 'message' )

    list_filter = ('status', 'date')

    search_fields = ['student_name']

    actions = ['make_confirmed' , 'make_declined']


    def save_model(self, request, obj, form, change):
        if change:  # only if this is an edit, not a brand new booking being created
            old_status = Booking.objects.get(pk=obj.pk).status
            super().save_model(request, obj, form, change)
            if old_status != obj.status:
                if obj.status == 'confirmed':
                    subject = 'Your tutoring session is confirmed'
                    message = f'Hi {obj.student_name}, your session with {obj.tutor.name} on {obj.date} has been confirmed.'
                elif obj.status == 'declined':
                    subject = 'Your tutoring session is declined'
                    message = f'Hi {obj.student_name}, your session with {obj.tutor.name} on {obj.date} has been declined.'
                else:
                    return
                send_mail(subject, message, 'noreply@tutorapp.com', [obj.email])
        else:
            super().save_model(request, obj, form, change)


    @admin.action(description='Mark selected bookings as Confirmed')
    def make_confirmed(self, request, queryset):
        queryset.update(status='confirmed')

        for booking in queryset:
            send_mail(
                'Your tutoring session is confirmed',
                f'Hi {booking.student_name}, your session with {booking.tutor.name} on {booking.date} has been confirmed.',
                'noreply@tutorapp.com',
                [booking.email]
            )

    @admin.action(description='Mark selected booking as Declined')
    def make_declined(self, request, queryset):
        queryset.update(status= 'declined')

        for booking in queryset:
            send_mail(
                'Your tutoring session is declined',
                f'Hi {booking.student_name}, your session with {booking.tutor.name} on {booking.date} has been declined.',
                'noreply@tutorapp.com',
                [booking.email]
            )

