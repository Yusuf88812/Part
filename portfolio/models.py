from django.db import models
from ckeditor.fields import RichTextField

class Profile(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="To'liq ism")
    title = models.CharField(max_length=200, verbose_name="Sarlavha (masalan: Full Stack Developer)")
    short_intro = models.TextField(verbose_name="Qisqa tanishtiruv")
    about_me = RichTextField(verbose_name="Men haqimda (to'liq)")
    image = models.ImageField(upload_to='profile/', verbose_name="Profil rasmi")
    github = models.URLField(blank=True, null=True, verbose_name="GitHub link")
    telegram = models.URLField(blank=True, null=True, verbose_name="Telegram link")
    linkedin = models.URLField(blank=True, null=True, verbose_name="LinkedIn link")
    resume = models.FileField(upload_to='resume/', blank=True, null=True, verbose_name="Rezyume (PDF)")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profil"

class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ko'nikma nomi")
    percentage = models.IntegerField(default=80, verbose_name="Foiz (0-100)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ko'nikma"
        verbose_name_plural = "Ko'nikmalar"

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Xizmat nomi")
    description = models.TextField(verbose_name="Tavsif")
    icon_class = models.CharField(max_length=100, default='fas fa-code', verbose_name="FontAwesome klassi (masalan: fas fa-code)")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Xizmat"
        verbose_name_plural = "Xizmatlar"

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Loyiha nomi")
    description = models.TextField(verbose_name="Qisqa tavsif")
    technologies = models.CharField(max_length=200, verbose_name="Texnologiyalar (vergul bilan ajrating)")
    image = models.ImageField(upload_to='projects/', verbose_name="Loyiha rasmi")
    link = models.URLField(verbose_name="Loyiha Havolasi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"

class Experience(models.Model):
    company = models.CharField(max_length=200, verbose_name="Kompaniya")
    position = models.CharField(max_length=200, verbose_name="Lavozim")
    start_date = models.CharField(max_length=100, verbose_name="Boshlanish vaqti")
    end_date = models.CharField(max_length=100, default="Hozirgacha", verbose_name="Tugash vaqti")
    description = models.TextField(verbose_name="Tavsif")

    def __str__(self):
        return f"{self.position} at {self.company}"

    class Meta:
        verbose_name = "Tajriba"
        verbose_name_plural = "Tajribalar"

class Education(models.Model):
    institution = models.CharField(max_length=200, verbose_name="Muassasa")
    degree = models.CharField(max_length=200, verbose_name="Daraja/Soha")
    start_date = models.CharField(max_length=100, verbose_name="Boshlanish vaqti")
    end_date = models.CharField(max_length=100, verbose_name="Tugash vaqti")

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    class Meta:
        verbose_name = "Ta'lim"
        verbose_name_plural = "Ta'lim"

class ContactMessage(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ism")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Mavzu")
    message = models.TextField(verbose_name="Xabar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqt")

    def __str__(self):
        return f"Message from {self.name}"

    class Meta:
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"
