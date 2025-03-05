from django.shortcuts import render
from .models import (
    Skill, Language, Certification, Education, 
    WorkExperience, Project, Interest, PersonalInfo
)
from django.contrib.auth.models import User

def home(request):
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        # If no personal info exists, create a default one
        user, _ = User.objects.get_or_create(
            username='admin',
            defaults={'email': 'example@example.com'}
        )
        personal_info = PersonalInfo.objects.create(
            user=user,
            job_title='Full Stack Developer | Software Engineer',
            location='City, Country',
            email='example@example.com',
            phone='+1234567890'
        )
    
    context = {
        'personal_info': personal_info,
        'skills': Skill.objects.all().order_by('order'),
        'languages': Language.objects.all(),
        'certifications': Certification.objects.all(),
        'education': Education.objects.all().order_by('-start_date'),
        'experiences': WorkExperience.objects.all().order_by('-start_date'),
        'projects': Project.objects.all(),
        'interests': Interest.objects.all(),
    }
    
    return render(request, 'home.html', context)