from django.shortcuts import render
from .models import ContactInformation, Education, Experience, Project, Skill

def resume_view(request):
    contact = ContactInformation.objects.first()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()

    context = {
        'contact': contact,
        'educations': educations,
        'experiences': experiences,
        'projects': projects,
        'skills': skills
    }

    return render(request, 'resume/resume_template.html', context)
def home_view(request):
    contact = ContactInformation.objects.first()  # Retrieve the contact info
    return render(request, 'resume/home.html', {'contact': contact})
