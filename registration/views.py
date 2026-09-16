from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from .models import Student
from .forms import StudentForm


def student_list(request):
    """READ - display all registered students."""
    students = Student.objects.all()
    return render(
        request,
        'registration/student_list.html',
        {'students': students}
    )


def student_create(request):
    """CREATE - register a new student."""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(
        request,
        'registration/student_form.html',
        {'form': form}
    )


def student_update(request, pk):
    """UPDATE - edit an existing student's information."""
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(
            request.POST,
            instance=student
        )
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'registration/student_form.html',
        {
            'form': form,
            'student': student
        }
    )


def student_delete(request, pk):
    """DELETE - remove a student record after confirmation."""
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(
        request,
        'registration/student_confirm_delete.html',
        {'student': student}
    )
