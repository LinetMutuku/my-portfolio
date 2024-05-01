from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
urlpatterns = [
    path('', views.home, name= 'home'),
     path('project_list', views.project_list, name='project_list'),
     path('about_me', views.about_me, name= 'about_me'),
     path('contact_me', views.contact_me, name='contact_me')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)