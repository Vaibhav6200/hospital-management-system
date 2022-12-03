


from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.shortcuts import get_object_or_404, render

from .models import Departments, Doctors


def home(request):
    dep = Departments.objects.all()
    doctors_list = Doctors.objects.all().filter(available=True)
    paginator = Paginator(doctors_list, 4)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        doctors_lst = paginator.page(page)
    except (EmptyPage, InvalidPage):
        doctors_lst = paginator.page(paginator.num_pages)
    return render(request, 'home.html',{"depar":dep,"doct":doctors_lst})
def aboutUs(request):
    return render(request, "about.html")
def departmentView(request,d_slug=None):
    d_page = get_object_or_404(Departments, id=d_slug)
    doc_list = Doctors.objects.all().filter(departments=d_slug, available=True)
    return render(request, 'depview.html',{'department':d_page,'doctor':doc_list})


def dashboard(request):
    doctors = Doctors.objects.all()
    doc_count = doctors.count()
    departments = Departments.objects.all()
    dep_count = departments.count()
    context = {
        "doc_count":doc_count,
        "dep_count":dep_count
    }
    return render(request, 'user_logined.html',context)
