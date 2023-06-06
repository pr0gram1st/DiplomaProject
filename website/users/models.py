from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField('Course Name', max_length=100)
    info = models.TextField('Course Info', default='SOME STRING')
    description = models.TextField('Course Description')
    html = models.TextField('Course HTML')
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    def __str__(self):
        return self.name

class My_User(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=100)
    surname = models.CharField("Surname", max_length=100)
    phone = models.CharField("Phone Number", max_length=12)
    date_of_birth = models.DateField("Date of birth")
    email = models.EmailField("Email")

    def __str__(self):
        return self.name


class Course_stats(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete= models.CASCADE)

