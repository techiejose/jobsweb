from django.db import models
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name= models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Job(models.Model):
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default='engineering')
    description = models.TextField()
    type = models.CharField(max_length=255)
    process= models.TextField()
    salary= models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    dateposted= models.DateField(auto_now_add=True)
    deadline= models.DateField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.company

    def get_absolute_url(self):
        return reverse('register')


class Account(models.Model):
    first_name=models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    proffesion = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)


    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('register')

#send notifications to registered members on posting of new job
@receiver(post_save, sender=Job)
def send_new_job_notification_email(sender, instance, created, **kwargs):

    # if a new officer is created, compose and send the email
    if created:
        company = instance.company if instance.company else "no name given"
        position = instance.position if instance.position else "no rank given"

        #filter emails
        email_receiver=Account.objects.values('email').filter(proffesion=position)
        subject = 'IS LOOKING FOR A'
        message = 'Hello, we have a job that you might be interested in!\n'
        message += 'POSITION: ' + position + '\n' + 'COMPANY: ' \
                  + company + '\n'

        send_mail(
            subject,
            message,
            'muthokajoseph10@gmail.com',
            [email_receiver],
            fail_silently=False,
        )

