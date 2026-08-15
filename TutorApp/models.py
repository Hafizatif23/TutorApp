from django.db import models

# Create your models here.
class Tutor(models.Model):

    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    bio = models.TextField()


class Booking(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

    StatusChoices = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('declined', 'Declined')
    ]

    status = models.CharField(max_length=50, choices=StatusChoices, default='pending')
    student_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(blank=False, null=False)
    date = models.DateField()
    message = models.TextField()
