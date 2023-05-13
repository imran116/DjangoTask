from django.db import models

# Create your models here.

class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='profile_picture/')
    profile_name = models.CharField(max_length=30)
    facebook_link = models.CharField(max_length=150)
    instagram_link = models.CharField(max_length=150)
    twitter_link = models.CharField(max_length=150)
    linkedin_link = models.CharField(max_length=150)
    skype_link = models.CharField(max_length=150)

    def __str__(self):
        return self.profile_name

class SliderText(models.Model):
    slider_text = models.CharField(max_length=30)

    def __str__(self):
        return self.slider_text

class About(models.Model):
    image = models.ImageField(upload_to='about/')
    about = models.TextField()
    title = models.TextField(max_length=40)
    title_desc_one = models.TextField()
    title_desc_second = models.TextField()
    birthday = models.DateField()
    website = models.CharField(max_length=150)
    phone = models.IntegerField()
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    degree = models.CharField(max_length=50)
    freelance = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Fact(models.Model):
    description = models.TextField()
    client_no = models.IntegerField()
    client_desc = models.CharField(max_length=100)
    project_no = models.IntegerField()
    project_desc = models.CharField(max_length=100)
    total_working_hour = models.IntegerField()
    working_hour_desc = models.CharField(max_length=100)
    worker_no = models.IntegerField()
    worker_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Skill(models.Model):
    skill_name = models.CharField(max_length=30)
    skill_percentage = models.IntegerField()

    def __str__(self):
        return self.skill_name

class Resume(models.Model):
    title = models.CharField(max_length=150)
    profession_name = models.CharField(max_length=150)
    year_range = models.CharField(max_length=30)
    work_type = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_resumeDesc(self):
        return self.resumedescription_set.all()


class ResumeDescription(models.Model):

    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.resume


class PortfolioApp(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title

class PortfolioCard(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title

class PortfolioWeb(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimonial/')
    name = models.CharField(max_length=40)
    designation = models.CharField(max_length=40)
    quote = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class Description(models.Model):

    skill_desc = models.TextField()
    resume_desc = models.TextField()
    portfolio_desc = models.TextField()
    service_desc = models.TextField()
    testimonial_desc = models.TextField()
    contact_desc = models.TextField()

    def __str__(self):
        return self.resume_desc

class Copyright(models.Model):
    name = models.CharField(max_length=50)
    designer_name = models.CharField(max_length=50)
    designer_link = models.CharField(max_length=150,null=True, blank=True)

    def __str__(self):
        return self.name








