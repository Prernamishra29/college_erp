from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def student_list(request):
    return render(request, 'students/student_list.html')  # Ensure this template exists
