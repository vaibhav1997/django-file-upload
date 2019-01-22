from django.db import models

# Create your models here.
class Name(models.Model):
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)

    def __str__(self):
        return self.firstName
        return self.lastName

class File(models.Model):
    # filename = models.CharField(max_length = 200)
    upload = models.FileField(upload_to = 'uploads/',)

    def __str__(self):
        return self.upload