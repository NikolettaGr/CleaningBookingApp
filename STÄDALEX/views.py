from django.shortcuts import render

def home(request):
    """Function enables user to view the home page."""
    return render(request, 'STÄDALEX/home.html')
