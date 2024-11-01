from django.db import models

class AccessRequirement (models.TextChoices):
    ANYONE =  'anyone', 'Anyone'
    EMAIL_REQUIRED = 'email', 'Email Required'
    DRAFT  = 'draft', 'Draft'

class PublishStatus(models.TextChoices):
    PUBLISHED = 'published', 'Pub'
    COMING_SOON = "soon", "Coming Soon" 
    DRAFT =  'draft', 'Draft'

def handle_upload(instance, filename):
    return  f"{filename}"

class Course(models.Model):
    title = models.CharField(max_length=120)
    description =  models.TextField(blank=(True),  null=(True))
    image =  models.ImageField(upload_to=handle_upload, blank=(True), null=(True))
    access = models.CharField(
        max_length=10,
        choices = AccessRequirement.choices,
        default = AccessRequirement.EMAIL_REQUIRED
    )
    status = models.CharField(
        max_length=14,
        choices = PublishStatus.choices,
        default = AccessRequirement.EMAIL_REQUIRED
    )

    @property
    def is_published(shelf):
        return  shelf.status == PublishStatus.PUBLISHED




