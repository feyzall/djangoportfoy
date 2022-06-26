from django.contrib import admin
from . models import Menu
from . models import Social
from . models import About
from . models import Skilss
from . models import Education
from . models import Portfolio
from . models import Testimonials
from . models import Experience

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('jop',)


@admin.register(Skilss)
class SkilssAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('name',)



@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('name',)