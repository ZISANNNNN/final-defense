from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import DeleteView
from .models import job, wishlist
from .models import all_cv
from .models import edit_profile_model
from .models import edit_profile_picture
from django.core.files.storage import FileSystemStorage
from .models import wishlist
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import edit_password_form
from django.contrib.auth.views import PasswordChangeView
from .models import apply_for_job


class change_password (PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile')


class home1 (ListView):
    model = job
    template_name = "index.html"
    ordering = ['-id']


def home2(request):
    return render(request, "index-02.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def support(request):
    return render(request, "support.html")


class job_page (ListView):
    template_name = "job-page.html"
    model = job
    ordering = ['-id']

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related


class wishlist_page (ListView):
    template_name = "wishlist.html"
    model = wishlist
    ordering = ['-id']

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related


class job_details (generic.DeleteView):
    model = job
    template_name = "job-details.html"
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(job_details, self).get_context_data(*args, **kwargs)
        context['job_list'] = job.objects.all()
        context['apply_job_list'] = apply_for_job.objects.all()
        return context


def resume(request):
    return render(request, "resume.html")


def pricing(request):
    return render(request, "pricing.html")


def browse_job(request):
    return render(request, "browse-jobs.html")


class profile (ListView):
    template_name = "profile.html"
    model = job
    ordering = ['-id']

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related

    def get_context_data(self, *args, **kwargs):
        context = super(profile, self).get_context_data(*args, **kwargs)
        context['profile_list'] = edit_profile_model.objects.all()
        context['profile_pic_list'] = edit_profile_picture.objects.all()
        context['all_cv_list'] = all_cv.objects.all()
        return context


def cv(request):
    return render(request, "cv_submit.html")


def job_post(request):
    if request.method == "POST":
        username = request.POST['username']
        title = request.POST['title']
        company = request.POST['company']
        location = request.POST['location']
        email = request.POST['email']
        name = request.POST['name']
        jobs = request.POST['job']
        category = request.POST['category']
        job_time = request.POST['job_time']
        job_database = job(username=username, email=email, name=name, jobs=jobs,
                           title=title, category=category, company=company, location=location, job_time = job_time)
        job_database.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def apply_job_form(request):
    if request.method == "POST":
        username = request.POST['username']
        post_id = request.POST['post_id']
        title = request.POST['title']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        education = request.POST['education']
        description = request.POST['description']
        apply_job_database = apply_for_job(username=username, post_id=post_id, title=title,
                                     name=name, phone=phone, email=email, education=education, description=description)
        apply_job_database.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def wishlist_post(request):
    if request.method == "POST":
        username = request.POST['username']
        title = request.POST['title']
        company = request.POST['company']
        location = request.POST['location']
        email = request.POST['email']
        name = request.POST['name']
        jobs = request.POST['job']
        category = request.POST['category']
        wishlist_database = wishlist(username=username, email=email, name=name, jobs=jobs,
                                     title=title, category=category, company=company, location=location)
        wishlist_database.save()
        return redirect ("wishlist_page")


def all_cv_form(request):
    if request.method == 'POST' or request.FILES['myfile']:
        username = request.POST['username']
        name = request.POST['name']
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        if all_cv.objects.filter(username=username).exists():
            return HttpResponse("You have already submitted your CV.")
        else:
            cv_database = all_cv(
                username=username, name=name, cv=myfile)
            cv_database.save()
            return render(request, 'profile.html', {
                'uploaded_file_url': uploaded_file_url
            })
    return redirect("profile")


# Authentication

def signinn(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Email or Password incorrect')

    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken")
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, password=password, email=email)
                user.save()
                login(request, user)
                return redirect('/')

        else:
            messages.error(request, 'Password not matched')

    return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect("/")


def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        category = request.POST['category']
        location = request.POST['location']
        Job_list = job.objects.filter(
            jobs__contains=search, category__contains=category, location__contains=location)
        return render(request, 'search.html', {'search': search, 'job_list': Job_list})
    else:
        return render(request, "search.html")


def edit_profile(request):
    return render(request, "edit_profile.html")


class profile_picture (ListView):
    template_name = "profile_picture.html"
    model = job
    ordering = ['-id']

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related

    def get_context_data(self, *args, **kwargs):
        context = super(profile_picture, self).get_context_data(
            *args, **kwargs)
        context['profile_list'] = edit_profile_model.objects.all()
        context['profile_pic_list'] = edit_profile_picture.objects.all()
        return context


def edit_profile_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        phone = request.POST['phone']
        address = request.POST['address']
        previous_job = request.POST['previous_job']
        your_field_of_job = request.POST['your_field_of_job']
        edit_profile_database = edit_profile_model(
            username=username, phone=phone, address=address, previous_job=previous_job, your_field_of_job=your_field_of_job)
        edit_profile_database.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def profile_pic_form(request):
    if request.method == 'POST' or request.FILES['myfile']:
        username = request.POST['username']
        if edit_profile_picture.objects.filter(username=username).exists():
            return HttpResponse("You can change your profile picture only one time.")
        else:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            edit_profile_database = edit_profile_picture(
                username=username, profile_picture=myfile)
            edit_profile_database.save()
            return render(request, 'profile.html', {
                'uploaded_file_url': uploaded_file_url
            })
    return redirect("profile")


class delete_profile_picture(DeleteView):
    model = edit_profile_picture
    template_name = 'profile_picture.html'
    fields = ['profile_picture']
    # success_url=reverse_lazy("comments/53")

    def get_context_data(self, *args, **kwargs):
        context = super(delete_profile_picture,
                        self).get_context_data(*args, **kwargs)
        context['edit_profile_picture_list'] = edit_profile_picture.objects.all()
        return context
    success_url = ("http://127.0.0.1:8000/profile/")


class your_cv (DeleteView):
    model = all_cv
    template_name = 'delete_cv.html'
    fields = ['profile_picture']
    # success_url=reverse_lazy("comments/53")

    def get_context_data(self, *args, **kwargs):
        context = super(your_cv, self).get_context_data(*args, **kwargs)
        context['all_cv_lisr'] = all_cv.objects.all()
        return context
    success_url = ("http://127.0.0.1:8000/profile/")


class edit_password (generic.UpdateView):
    model = User
    form_class = edit_password_form
    template_name = 'edit_password.html'
    success_url = reverse_lazy('edit_password')

    def get_object(self):
        return self.request.user
