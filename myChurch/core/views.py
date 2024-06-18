from django.shortcuts import render, HttpResponse, redirect
from item.models import Category, Item
from event.models import Event
from project.models import Project
from official.models import Official
from gallery.models import Gallery
from review.models import Review
from django.contrib import messages
from .models import Contact, Payment, AccDet

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    projects = Project.objects.all()
    officials = Official.objects.all()
    gallerys = Gallery.objects.all()
    reviews = Review.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
        'projects': projects,
        'officials': officials,
        'gallerys': gallerys,
        'reviews': reviews,
    })

def event(request):
    events = Event.objects.all()
    return render(request, 'core/event.html', {'events': events})


def project(request):
    projects = Project.objects.all()
    return render(request, 'core/project.html', {'projects': projects})

def official(request):
    officials = Official.objects.all()
    return render(request, 'core/official.html', {'officials': officials})

def about(request):
    items = Item.objects.all()
    return render(request, 'core/about.html', {
        'items': items,
    })

def gallery(request):
    gallerys = Gallery.objects.all()
    return render(request, 'core/gallery.html', {'gallerys': gallerys})

def review(request):
    reviews = Review.objects.all()
    return render(request, 'core/reviews.html', {'reviews': reviews})

def account(request):
    acc = AccDet.objects.all()
    return render(request, 'core/payment.html', {'acc': acc})



def contact(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        phone = request.POST.get('phone')
        description= request.POST.get('description')
        query=Contact(name=fname,email=femail,phoneNumber=phone,description=description)
        query.save()
        messages.info(request,"Thanks For Reaching Us! We will get back to you soon....")
        return redirect('/contact')
    return render(request, 'core/contact.html', {})


def payment(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        query = Payment(name=fname, description=description, image=image)
        query.save()
        messages.info(request, "Thanks For Reaching Us! We will get back to you soon....")
        return redirect('/payment')
    return render(request, 'core/payment.html', {})