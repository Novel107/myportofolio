from django.shortcuts import render

from main.models import Experience


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