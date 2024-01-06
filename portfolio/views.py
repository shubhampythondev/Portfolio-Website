from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Contact, Blogs, Internship


# Create your views here.
def home(request):
    return render(request, 'home.html')


def handleblog(request):
    posts = Blogs.objects.all()
    context = {"posts": posts}
    return render(request, 'handleblog.html', context)


def about(request):
    return render(request, 'about.html')


def Internshipdetails(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please login to access this page")
        return redirect("/auth/login/")

    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fusn = request.POST.get('usn')
        fcollege = request.POST.get('cname')
        foffer = request.POST.get('offer')
        fstartdate = request.POST.get('startdate')
        fenddate = request.POST.get('enddate')
        fprojreport = request.POST.get('projreport')

        # converting to upper case
        fname = fname.upper()
        femail = femail.upper()
        fusn = fusn.upper()
        fcollege = fcollege.upper()
        foffer = foffer.upper()
        fstartdate = fstartdate.upper()
        fenddate = fenddate.upper()
        fprojreport = fprojreport.upper()

        #
        check1=Internship.objects.filter(USN=fusn)
        check2=Internship.objects.filter(email=femail)

        if check1 or check2:
            messages.success(request,"Form is submitted Successful !")
            return redirect('/Internshipdetails')

        query = Internship(fullname=fname, email=femail, USN=fusn, college_name=fcollege, offer_status=foffer,
                           start_date=fstartdate, end_date=fenddate, proj_report=fprojreport)
        query.save()
        messages.success(request, "Form is Submitted Successfull")
        return redirect('/Internshipdetails')

    return render(request, 'internship.html')


def contact(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fphoneno = request.POST.get('num')
        fdesc = request.POST.get('desc')
        query = Contact(name=fname, email=femail, phonenumber=fphoneno, description=fdesc)
        query.save()
        messages.success(request, "Thanks for Contacting. We will get by you Soon !! ")
        return redirect('/contact')

    return render(request, 'contact.html')
