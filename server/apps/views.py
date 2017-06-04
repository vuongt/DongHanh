from django.shortcuts import render
from django.views.generic import UpdateView, DetailView, ListView
from .models import University, Candidate, Jury, Evaluation

# Create your views here.


class UniversityListView(ListView):
    model = University
    template_name = 'apps/base.html'