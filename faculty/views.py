from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def faculty_home(request):
    return render(request, 'faculty/faculty_home.html')  # Ensure this template exists


