from django.contrib import admin

from .models import Course
from .models import Course_stats
from .models import My_User

admin.site.register(Course)
admin.site.register(Course_stats)
admin.site.register(My_User)
# Register your models here.
