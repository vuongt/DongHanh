from django.views.generic import DetailView, CreateView, UpdateView, ListView, RedirectView
from .models import University
from .forms import UniversityUpdateForm

# Create your views here.
from django.http import HttpResponse


class UniversityListView(ListView):
    model = University
    template_name = "university/index.html"


class UniversityUpdateView(UpdateView):
    model = University
    template_name = "form.html"
    form_class = UniversityUpdateForm

