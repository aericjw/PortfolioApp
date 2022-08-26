from django.contrib import admin
from Portfolio.models import About, Skill, Experience, Project, ContactForm
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    fieldsets = [
        (About, {'fields': ['about_text']})
    ]
    list_display = ['about_text']
admin.site.register(About, AboutAdmin)

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (Project, {'fields': ['name', 'description', 'icon']})
    ]
    list_display = ('name', 'description', 'icon')
    search_fields = ['name']

admin.site.register(Project, ProjectAdmin)

class SkillAdmin(admin.ModelAdmin):
    fieldsets = [
        (Skill, {'fields': ['name']})
    ]
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Skill, SkillAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    fieldsets = [
        (Experience, {'fields': ['start_date', 'end_date', 'title', 'company', 'location', 'description']})
    ]
    list_display = ('start_date', 'end_date', 'title', 'company', 'location', 'description')
    search_fields = ['company']
admin.site.register(Experience, ExperienceAdmin)

class FormAdmin(admin.ModelAdmin):
    fieldsets = [
        (ContactForm, {'fields': ['name', 'email', 'subject', 'message']})
    ]
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ['name', 'email']
admin.site.register(ContactForm, FormAdmin)