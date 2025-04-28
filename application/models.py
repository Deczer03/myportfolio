from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Contact(models.Model):
    """Model for storing contact form submissions."""
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Submission Date")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
    
    def __str__(self):
        return f"Message from {self.name} ({self.email}) on {self.created_at.strftime('%Y-%m-%d %H:%M')}"


class Project(models.Model):
    """Model for storing project information."""
    title = models.CharField(max_length=200, verbose_name="Project Title")
    description = models.TextField(verbose_name="Project Description")
    image = models.ImageField(upload_to='projects/', verbose_name="Project Image")
    technologies_used = models.CharField(max_length=500, verbose_name="Technologies Used",
                                      help_text="Enter technologies separated by commas")
    project_link = models.URLField(blank=True, null=True, verbose_name="Project URL")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created Date")
    is_featured = models.BooleanField(default=False, verbose_name="Featured on Homepage")

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])

    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies_used.split(',')]
