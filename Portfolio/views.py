from django.shortcuts import render
from Portfolio.models import About, Skill, Experience, Project, ContactForm

def homepage(request):
    abouts = About.objects.all()
    skills = Skill.objects.all()
    exp = Experience.objects.all()
    project = Project.objects.all()
    form = ContactForm.objects.all()
    
    for e in exp:
        e.start_date = e.start_date.strftime("%m/%Y")
        e.end_date = e.end_date.strftime("%m/%Y")
    
    context = {
        'abouts': abouts,
        'skills': skills,
        'experience': exp,
        'projects': project,
        'form': form
    }
    return render(request, 'index.html', context)
