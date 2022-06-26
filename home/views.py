from django.shortcuts import render
from . models import Menu,Social,About,Skilss,Education,Portfolio,Testimonials,Experience

def index(request):
    menu=Menu.objects.all()
    social=Social.objects.all()
    about=About.objects.all()
    skilss=Skilss.objects.all()
    education=Education.objects.all()
    portfolio=Portfolio.objects.all()
    experience=Experience.objects.all()
    testimonials=Testimonials.objects.all()
    context = {
        'menu': menu,
        'social': social,
        'about':about,
        'skilss':skilss,
        'education':education,
        'portfolio':portfolio,
        'testimonials':testimonials,
        'experience':experience,
    }
    return render(request, 'index.html',context)
