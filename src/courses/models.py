from django.db import models

class AccessRequirement (models.TextChoices):
    ANYONE =  'anyone', 'Anyone'
    EMAIL_REQUIRED = 'email_required', 'Email Required'




class PublishStatus(models.TextChoices):
    PUBLISHED = 'published', 'Pub'
    COMING_SOON = "soon", "Coming Soon" 
    DRAFT =  'draft', 'Draft'


class Coourse(models.Model):
    title = models.CharField(max_length=120)
    description =  models.TextField(blank=(True),  null=(True))
    # image =
    access = models.CharField(
        max_length=10,
        choices = AccessRequirement.choices,
        default = PublishStatus.DRAFT
    )
    status = models.CharField(
        max_length=10,
        choices = PublishStatus.choices,
        default = AccessRequirement.DRAFT
    )

    @property
    def is_published(shelf):
        return  shelf.status == PublishStatus.PUBLISHED




