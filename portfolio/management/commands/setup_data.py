from django.core.management.base import BaseCommand
from portfolio.models import Profile, Skill, Project, Service, Experience, Education
from django.core.files.base import ContentFile
import requests

class Command(BaseCommand):
    help = 'Populates the database with initial developer portfolio data'

    def handle(self, *args, **kwargs):
        # 1. Profile
        profile, created = Profile.objects.get_or_create(
            full_name="Yusuf Sunnatov",
            defaults={
                "title": "Full Stack Django Developer",
                "short_intro": "Professional software developer specializing in high-performance web applications and backend systems using Python & Django.",
                "about_me": "<p>Men Yusuf Sunnatovman, tajribali Full Stack dasturchi. Men asosan Python va Django texnologiyalari yordamida murakkab va kengayuvchan veb-tizimlarni ishlab chiqaman.</p>",
                "github": "https://github.com/yusuf",
                "telegram": "https://t.me/yusuf_dev",
                "linkedin": "https://linkedin.com/in/yusuf"
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS("Profile created!"))

        # 2. Skills
        skills = [
            ("Python", 95),
            ("Django", 90),
            ("JavaScript", 85),
            ("HTML5/CSS3", 90),
            ("REST APIs", 92),
            ("PostgreSQL", 88)
        ]
        for name, pct in skills:
            Skill.objects.get_or_create(name=name, defaults={"percentage": pct})
        self.stdout.write(self.style.SUCCESS("Skills populated!"))

        # 3. Services
        services = [
            ("Web Development", "Zamonaviy va responsive veb-saytlar yaratish.", "fas fa-code"),
            ("Backend Development", "Murakkab server-side tizimlarni loyihalash.", "fas fa-server"),
            ("Django Web Apps", "Django frameworkida to'liq veb-ilovalarni ishlab chiqish.", "fab fa-python"),
            ("Frontend", "Mobil va veb platformalar uchun zamonaviy interfeyslar.", "fas fa-laptop-code")
        ]
        for title, desc, icon in services:
            Service.objects.update_or_create(title=title, defaults={"description": desc, "icon_class": icon})
        self.stdout.write(self.style.SUCCESS("Services populated!"))

        # 4. Experience
        Experience.objects.update_or_create(
            position="Fronted developer",
            company="Mars IT school",
            defaults={
                "start_date": "2026",
                "end_date": "Hozirgacha",
                "description": ""
            }
        )
        Experience.objects.update_or_create(
            position="Backend Developer",
            company="Mars IT school",
            defaults={
                "start_date": "2025",
                "end_date": "2026",
                "description": ""
            }
        )

        # 5. Education
        Education.objects.update_or_create(
            degree="Mars IT school ",
            institution="Tashkent it academy",
            defaults={
                "start_date": "2025",
                "end_date": "2026"
            }
        )

        # 6. Projects (including the special one)
        Project.objects.update_or_create(
            title="Online Test Tizimi",
            defaults={
                "description": "Murakkab test va imtihon tizimi (Django/JS).",
                "technologies": "Django, JavaScript, PostgreSQL",
                "link": "https://testyusuf.pythonanywhere.com"
            }
        )
        Project.objects.update_or_create(
            title="FastFood",
            defaults={
                "description": "FastFood bron va zakaz",
                "technologies": "Django",
                "link": "https://fastfoodyusuf.pythonanywhere.com"
            }
        )
        
        self.stdout.write(self.style.SUCCESS("All data populated successfully!"))
