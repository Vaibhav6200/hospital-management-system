
from accountAPP.models import RegisteredUser
from django.contrib import messages
from django.shortcuts import redirect, render
from hospitalAPP.models import Departments, Doctors

from .models import Booking


def booking(request):
    doctors =Doctors.objects.all()
    department =Departments.objects.all()
    context = {
                'doc':doctors,
                'dep':department
            }
    if request.method == "POST":

        name = request.POST['fullname']
        pic = request.POST['photo']
        num = request.POST['number']
        d = request.POST['date']
        t = request.POST['time']
        rea = request.POST['reson']
        depname = request.POST.get('dep',False)
        docname = request.POST.get('doc',False)
        bok = Booking(full_name=name,profile_photo=pic,contact_number=num,booking_date=d,booking_time=t,deasease=rea,doc_name=docname,dep_name=depname)
        bok.save()

        fname = name.split(" ")[0]
        url = fname+'/receipt'
        return redirect(url)
    return render(request,"booking.html",context)


def receipt(request,fname):
    bo = Booking.objects.all().filter(full_name=fname)
    re = RegisteredUser.objects.all()
    return render(request,'receipt.html',{"bo":bo,"re":re})
