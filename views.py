from django.views.generic import TemplateView, ListView, DetailView, FormView, TemplateView #deleteview??
from personal.models import Entry, Project
from .forms import EntryForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


#main homepage
class EPHomeView(TemplateView):
    template_name = "homepage.html"

#bill wurtz style list of all entries
class EntryListView(ListView):
    model = Entry
    context_object_name = 'all_entries'
    template_name = "entrieslist.html"

    def get_queryset(self):
        return super().get_queryset().order_by('-date')  

#view an entry from queryset
class EntryView(DetailView):
    model = Entry
    template_name = "entryview.html"

#my eyes only -- create an entry, CANNOT EDIT OR DELETE 
class EntryCreate(FormView):
    template_name = "entrycreate_form.html"
    form_class = EntryForm

    #save entry
    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    #after creating an entry send me back to entries
    def get_success_url(self):
        return reverse("entries")
        
    #only i can create entries!!!
    def test_func(self):
        return self.request.user.is_superuser

class ProfessionalTemplateView(TemplateView):
    model = None
    template_name = "professional.html"

class ProjectListView(ListView):
    model = Project
    context_object_name = 'all_projects'

def information_is_beautiful_redirect(request):
    return redirect("https://informationisbeautiful.net", permanent=True)

def github_redirect(request):
    return redirect("https://github.com/emei18", permanent=True)
    

    
