from django.contrib import admin
from django.urls import path, include
from . import views
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='index'),
    path('about/', views.about , name='about'),
    path('contact/', views.contact , name='contact'),
    path('courses/', views.courses , name='courses'),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('courses/',include('courses.urls')),
    path('quiz/', views.quiz, name='quiz')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
