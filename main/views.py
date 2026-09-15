from django.shortcuts import render, redirect
from main.models import Experience, Education
from main.forms import EducationForm


def show_main(request):
    context = {
        "name": "Muhammad Fachri Novelino",
        "nickname":"Fachri",
        "npm": "2506618881",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada Software Enginer dan Cyber Security."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Muhammad Fachri Novelino",
        "nickname": "Fachri",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    education_list = Education.objects.all()

    context = {
        "nickname": "Fachri",
        'education_list': education_list,
    }

    return render(request, 'education.html', context)

def create_education(request):
    form = EducationForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_education')

    context = {
        'form': form,
        'nickname': 'Fachri',
    }
    return render(request, "create_education.html", context)