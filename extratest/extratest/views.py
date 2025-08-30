from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User  
from django.contrib import messages

# Import models
from header.models import All
from footer.models import Allinfo,Designation,Signup
from home.models import Carousel,About
from service.models import Redirect,Serviceinfo,Listinfo
from menu.models import Menustart,Category,Pricing
from reservation.models import Reservoninfo,Table
from testimonial.models import Testiinfo
from contact.models import Continfo,Form,Conlast
from contact.forms import ContactForm


def home(request):
    all=All.objects.first()
    allinfo=Allinfo.objects.first()
    d=Designation.objects.first()
    carousel=Carousel.objects.first()
    about=About.objects.first()
    # signup in footer
    if request.method == "POST":
        email = request.POST.get("email")

        if email:
            if Signup.objects.filter(email=email).exists():
                messages.success(request, "You are already signup with this mail. User another!")
            else:
                Signup.objects.create(email=email)
                messages.success(request, f"{email} saved successfully!")
        else:
            messages.error(request, "Please enter a valid email.")

        return redirect("home") 
    
    data={
        'all':all,
        'allinfo':allinfo,
        'd':d,
        'carousel':carousel,
        'about':about,
    }
    return render(request, 'index.html',data)



def service(request):
    all=All.objects.first()
    allinfo=Allinfo.objects.first()
    d=Designation.objects.first()
     # signup in footer
    if request.method == "POST":
        email = request.POST.get("email")

        if email:
            if Signup.objects.filter(email=email).exists():
                messages.success(request, "You are already signup with this mail. User another!")
            else:
                Signup.objects.create(email=email)
                messages.success(request, f"{email} saved successfully!")
        else:
            messages.error(request, "Please enter a valid email.")

        return redirect("home") 
    
    redirect=Redirect.objects.first()
    serviceinfo=Serviceinfo.objects.first()
    listinfo=Listinfo.objects.all()
    data={
        'all':all,
        'allinfo':allinfo,
        'd':d,
        'redirect':redirect,
        'serviceinfo':serviceinfo,
        'listinfo':listinfo,
    }
    return render(request, 'service.html',data)



def menu(request):
    all=All.objects.first()
    allinfo=Allinfo.objects.first()
    d=Designation.objects.first()
     # signup in footer
    if request.method == "POST":
        email = request.POST.get("email")

        if email:
            if Signup.objects.filter(email=email).exists():
                messages.success(request, "You are already signup with this mail. User another!")
            else:
                Signup.objects.create(email=email)
                messages.success(request, f"{email} saved successfully!")
        else:
            messages.error(request, "Please enter a valid email.")

        return redirect("home") 
    
    menustart=Menustart.objects.first()
    category=Category.objects.first()
    pricing=Pricing.objects.all()
    data={
        'all':all,
        'allinfo':allinfo,
        'd':d,
        'menustart':menustart,
        'category':category,
        'pricing':pricing,
    }
    return render(request, 'menu.html',data)



def reservation(request):
    all=All.objects.first()
    allinfo=Allinfo.objects.first()
    d=Designation.objects.first()
     # signup in footer
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        date = request.POST.get("date")
        time = request.POST.get("time")
        number = request.POST.get("number")

        if email:
            if Signup.objects.filter(email=email).exists():
                messages.success(request, "You are already signup and also book the table with this mail. User another mail for table booking!")
            elif name:
                Signup.objects.create(name=name,email=email,date=date,time=time,number=number)
                messages.success(request, f"{name} book the table sucessfully with {date}")
            else:
                Signup.objects.create(email=email)
                messages.success(request, f"{email} saved successfully! You are signup with this mail.")
        else:
            messages.error(request, "Please enter a valid email.")

        return redirect("reservation") 
    
    reservon=Reservoninfo.objects.first()
    table=Table.objects.first()
    data={
        'all':all,
        'allinfo':allinfo,
        'd':d,
        'reservon':reservon,
        'table':table,
    }
    return render(request, 'reservation.html',data)



def testimonial(request):
    all=All.objects.first()
    allinfo=Allinfo.objects.first()
    d=Designation.objects.first()
     # signup in footer
    if request.method == "POST":
        email = request.POST.get("email")

        if email:
            if Signup.objects.filter(email=email).exists():
                messages.success(request, "You are already signup with this mail. User another!")
            else:
                Signup.objects.create(email=email)
                messages.success(request, f"{email} saved successfully!")
        else:
            messages.error(request, "Please enter a valid email.")

        return redirect("home") 
    
    info=Testiinfo.objects.first()

    # Fetch all table bookings
    reservations = Signup.objects.all().order_by('id') 
    data={
        'all':all,
        'allinfo':allinfo,
        'd':d,
        'info':info,
        'reservations':reservations,
    }
    return render(request, 'testimonial.html',data)



def contact(request):
    all = All.objects.first()
    allinfo = Allinfo.objects.first()
    d = Designation.objects.first()
    info = Continfo.objects.first()
    last = Conlast.objects.first()

    if request.method == "POST":
        # Check if contact form submitted
        if "name" in request.POST and "subject" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")

            if Form.objects.filter(name=name, subject=subject).exists():
                messages.warning(request, "Your message is already saved with this name & subject. Use another!")
            else:
                Form.objects.create(name=name, email=email, subject=subject, message=message)
                messages.success(request, f"Contact form saved successfully with {name}")

        # Check if footer signup submitted
        elif "email" in request.POST:
            email = request.POST.get("email")
            if Signup.objects.filter(email=email).exists():
                messages.success(request, "You are already signup with this mail. Use another!")
            else:
                Signup.objects.create(email=email)
                messages.success(request, f"{email} saved successfully!")

        return redirect("contact")

    data = {
        'all': all,
        'allinfo': allinfo,
        'd': d,
        'info': info,
        'last':last,
    }
    return render(request, 'contact.html', data)

