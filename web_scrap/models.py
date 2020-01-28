from django.db import models

# Create your models here.


class JobsData(models.Model):
    job_title = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    experience = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    skill_set = models.TextField(null=True, blank=True)
    salary = models.CharField(max_length=255, null=True, blank=True)
    posted_date = models.CharField(max_length=255, null=True, blank=True)
    job_url = models.TextField(null=True, blank=True)
    job_site = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.job_title

