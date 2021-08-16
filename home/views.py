from django.shortcuts import render
from django.utils import db_connector

# Create your views here.

def index(request):
    """ A view to display the index page """
    return render(request, 'home/index.html')