from django.shortcuts import render, redirect
from main.models import Experience, Education
from main.forms import EducationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers


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

def delete_education(request, id):
    education = Education.objects.get(pk=id)
    education.delete()
    return HttpResponseRedirect(reverse('main:show_education'))

def show_xml(request):
    data = Education.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Education.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Education.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Education.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")