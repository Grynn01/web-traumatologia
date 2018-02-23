from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('itinerario/', views.itinerario, name='itinerario'),
    path('signup/', views.signup_new, name='signup new'),
    path('contact/', views.contact_new, name='contact new'),
    path('signup/done/', views.signup_done, name='signup done'),
    path('contact/done/', views.contact_done, name='contact done'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
