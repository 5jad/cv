from django.contrib import admin
from .models import (
    Skill, Language, Certification, Education, 
    WorkExperience, WorkResponsibility, Project, 
    ProjectTechnology, Interest, PersonalInfo
)

class WorkResponsibilityInline(admin.TabularInline):
    model = WorkResponsibility
    extra = 1

class WorkExperienceAdmin(admin.ModelAdmin):
    inlines = [WorkResponsibilityInline]
    list_display = ('title', 'company', 'start_date', 'end_date', 'is_current')

class ProjectTechnologyInline(admin.TabularInline):
    model = ProjectTechnology
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectTechnologyInline]
    list_display = ('title',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')

class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'date_obtained', 'expiry_date')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date')

class InterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_class')

admin.site.register(Skill, SkillAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(PersonalInfo)
