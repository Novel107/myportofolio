import datetime
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Experience, Education
from main.forms import EducationForm, ExperienceForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Muhammad Fachri Novelino",
        "nickname":"Fachri",
        "npm": "2506618881",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada Software Enginer dan Cyber Security."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    is_editor = request.user.groups.filter(name='Editor').exists() if request.user.is_authenticated else False
    
    context = {
        "name": "Muhammad Fachri Novelino",
        "nickname": "Fachri",
        "is_editor": is_editor, 
    }
    return render(request, "experience.html", context)


def show_education(request):
    education_list = Education.objects.all()

    context = {
        "nickname": "Fachri",
        'education_list': education_list,
    }

    return render(request, 'education.html', context)


@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = EducationForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_education')

    context = {
        'form': form,
        'nickname': 'Fachri',
    }
    return render(request, "create_education.html", context)


@login_required(login_url="/login/")
def delete_education(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

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


# Create experience

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ExperienceForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')

    context = {
        'form': form,
        'nickname': 'Fachri',
    }
    return render(request, "create_experience.html", context)


@login_required(login_url="/login/")
def update_experience(request, id):
    is_editor = request.user.groups.filter(name='Editor').exists()
    
    if not (request.user.is_superuser or is_editor):
        raise PermissionDenied

    experience = Experience.objects.get(pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')
    
    context = {
        'form': form,
        'nickname': 'Fachri',
    }
    return render(request, "update_experience.html", context)


@login_required(login_url="/login/")
def delete_experience(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = Experience.objects.get(pk=id)
    experience.delete()
    return HttpResponseRedirect(reverse('main:show_experience'))


def get_experiences_json(request):
    # Ambil semua experience dan gabungkan relasi starred_by agar lebih efisien
    experiences = Experience.objects.prefetch_related('starred_by').all()
        
    # Konstruksi data JSON secara manual
    data = []
    for experience in experiences:
        starred_users = experience.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])
        
        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.get_category_display(), # Mengambil label dari pilihan kategori
                "is_ongoing": experience.is_ongoing,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })
        
    return JsonResponse(data, safe=False)



def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        'form': form,
        'nickname': 'Fachri',
        'name': 'Muhammad Fachri Novelino'
    }
    return render(request, "register.html", context)

@login_required(login_url="/login/")
@require_POST
def add_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse({"status": "error", "message": "Akses ditolak"}, status=403)

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save(commit=False)
        experience.title = strip_tags(experience.title)
        experience.description = strip_tags(experience.description)
        experience.save()
        
        return JsonResponse({"status": "success", "message": "Pengalaman berhasil ditambahkan!"}, status=201)
    
    return JsonResponse({"status": "error", "message": form.errors}, status=400)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
        
    context = {
        'form': form,
        'nickname': 'Fachri',
        'name': 'Muhammad Fachri Novelino'
    }
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response


@login_required(login_url="/login/")
def toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    
    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)
            
    return redirect("main:show_experience")