from django.contrib import admin
from .models import ContactInformation, Education, Experience, Project, Skill

admin.site.register(ContactInformation)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Skill)
