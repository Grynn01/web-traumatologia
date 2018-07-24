from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_new, name='signup new'),
    path('contact/', views.contact_new, name='contact new'),
    path('signup_done/', views.signup_done, name='signup done'),
    path('contact_done/', views.contact_done, name='contact done'),
    path('vitae/', views.pdf_view, name='pdf view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
