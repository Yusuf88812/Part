from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, Service, Experience, Education, ContactMessage
from .utils import send_telegram_message

def index(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all().order_by('-percentage')
    projects = Project.objects.all()
    services = Service.objects.all()
    experiences = Experience.objects.all().order_by('-id')
    educations = Education.objects.all().order_by('-id')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            # Send Telegram Notification
            send_telegram_message(name, email, subject, message)
            
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi! Tez orada javob beraman.")
            return redirect('index')
        else:
            messages.error(request, "Iltimos, barcha maydonlarni to'ldiring.")

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'services': services,
        'experiences': experiences,
        'educations': educations,
    }
    return render(request, 'portfolio/index.html', context)
