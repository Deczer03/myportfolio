from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact, Project
from django import forms

# Create your views here.

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 5}),
        }

def index(request):
    # Get up to 3 featured projects for the homepage
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    return render(request, 'index.html', {
        'featured_projects': featured_projects
    })

def about(request):
    return render(request, 'about.html')

def project_list(request):
    # Get all projects, ordered by creation date
    projects = Project.objects.all()
    return render(request, 'project_list.html', {
        'projects': projects
    })

def project_detail(request, pk):
    # Get the specific project or return 404 if not found
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {
        'project': project
    })

def contact_form(request):
    """View for handling the contact form."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # Send an email notification
            send_mail(
                f'New contact form submission from {contact.name}',
                f'Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}',
                settings.EMAIL_HOST_USER,  # Using the Gmail address as sender
                [settings.CONTACT_EMAIL_RECIPIENT],
                fail_silently=False,
            )
            
            return redirect(reverse('contact_success'))
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact_form.html', {
        'form': form,
    })

def contact_success(request):
    """View for the contact success page."""
    return render(request, 'contact/contact_success.html')
