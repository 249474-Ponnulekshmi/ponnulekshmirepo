from django.urls import path
from .import views

urlpatterns = [
    path('emp/', views.details, name='emp_details'),
    path('jumble/', views.jumble_words, name='jumble')
]
