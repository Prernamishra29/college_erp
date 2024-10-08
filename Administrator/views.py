from django.shortcuts import render, redirect
from .models import Faculty
from .models import Student

# Function-based view for the Administrator page
def admin_view(request):
    # You can pass data to the template here if needed
    return render(request, 'admin_page.html')

# View to list and manage faculty
def manage_faculty(request):
    faculty_list = Faculty.objects.all()
    return render(request, 'administrator/manage_faculty.html', {'faculty_list': faculty_list})

# View to add new faculty
def add_faculty(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        department = request.POST['department']
        Faculty.objects.create(name=name, email=email, department=department)
        return redirect('administrator:manage_faculty')
    return render(request, 'administrator/manage_faculty.html')

# View to update faculty details
def update_faculty(request, faculty_id):
    faculty = Faculty.objects.get(id=faculty_id)
    if request.method == 'POST':
        faculty.name = request.POST['name']
        faculty.email = request.POST['email']
        faculty.department = request.POST['department']
        faculty.save()
        return redirect('administrator:manage_faculty')
    return render(request, 'administrator/update_faculty.html', {'faculty': faculty})

# View to delete faculty
def delete_faculty(request, faculty_id):
    faculty = Faculty.objects.get(id=faculty_id)
    faculty.delete()
    return redirect('administrator:manage_faculty')


# View to list and manage students
def manage_students(request):
    student_list = Student.objects.all()
    return render(request, 'administrator/manage_student.html', {'student_list': student_list})

# View to add new student
def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        course = request.POST['course']
        year = request.POST['year']
        Student.objects.create(name=name, email=email, course=course, year=year)
        return redirect('administrator:manage_students')
    return render(request, 'administrator/manage_student.html')

# View to update student details
def update_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.year = request.POST['year']
        student.save()
        return redirect('administrator:manage_students')
    return render(request, 'administrator/update_student.html', {'student': student})

# View to delete student
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('administrator:manage_students')