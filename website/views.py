import views as views
from django.contrib import messages
from django.core.mail import message
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from website import forms
from website.models import Profile, SliderText, About, Fact, Skill, Resume, PortfolioApp, PortfolioCard, PortfolioWeb, \
    Service, Testimonial, Description, Copyright


# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['profiles'] = Profile.objects.first()
        context['sliderTexts'] = SliderText.objects.first()
        context['abouts'] = About.objects.first()
        context['facts'] = Fact.objects.first()
        context['skills'] = Skill.objects.all()
        context['resumes'] = Resume.objects.all()
        context['portfolioapps'] = PortfolioApp.objects.all()
        context['portfoliocards'] = PortfolioCard.objects.all()
        context['portfoliowebs'] = PortfolioWeb.objects.all()
        context['services'] = Service.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        context['descriptions'] = Description.objects.first()
        context['copyrights'] = Copyright.objects.first()

        return context

class ContactView(View):

    def post(self,request):
        form = forms.ContactForm(data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Message Sent!")
        else:
            messages.error(request, "Your Message Not Sent!")

        return redirect('/')


