from django.db import models

# Contact Information Model
class ContactInformation(models.Model):
    email = models.EmailField()
    github = models.URLField()
    linkedin = models.URLField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.email

# Education Model
class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    graduation_date = models.CharField(max_length=50)  # E.g., "Jul 2023"
    coursework = models.TextField()

    def __str__(self):
        return self.degree + " from " + self.institution

# Experience Model
class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.CharField(max_length=50)  # E.g., "Jul 2023"
    end_date = models.CharField(max_length=50)  # E.g., "Aug 2024"
    responsibilities = models.TextField()

    def __str__(self):
        return self.position + " at " + self.company

# Project Model
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.CharField(max_length=50)  # E.g., "Aug 2022"

    def __str__(self):
        return self.title

# Skill Model
class Skill(models.Model):
    skill_name = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name
