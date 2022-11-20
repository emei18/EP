from django.urls import path 
from django.contrib import admin
from . import views
from personal.views import EPHomeView, EntryListView, EntryView, EntryCreate, ProfessionalTemplateView, information_is_beautiful_redirect, github_redirect

urlpatterns = [
    path('', EPHomeView.as_view(), name='home'),
    path('entries/', EntryListView.as_view(), name='entries'),
    path('entries/<int:pk>/', EntryView.as_view(), name='entry'),
    path('entry/create/', EntryCreate.as_view(), name='entry-create'),
    path('professional/', ProfessionalTemplateView.as_view(), name='professional'),
    path('infoisbeaut/', view=information_is_beautiful_redirect, name="InfoisBeaut"),
    path('github/', view=github_redirect, name="GitHub"),
]