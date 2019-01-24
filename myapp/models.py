from django.db import models

# Create your models here.
class Name(models.Model):
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)

    def __str__(self):
        return self.firstName ,self.lastName
        # return self.lastName

def get_upload_path(instance, filename):
    name, ext = filename.split('.')
    if(ext == 'pdf') or ('doc' in ext) or (ext == 'txt'):
        file_path = 'uploads/documents/{fname}.{ext}'.format(fname = name, ext = ext)
    elif('jpg' in ext) or (ext == 'png'):
        file_path = 'uploads/images/{fname}.{ext}'.format(fname = name, ext = ext)
    elif(ext == 'html') or (ext == 'py') or (ext == 'js'):
        file_path = 'uploads/dev/{fname}.{ext}'.format(fname = name, ext = ext)

    return file_path

class File(models.Model):
    # filename = models.CharField(max_length = 200)
    
    upload = models.FileField(upload_to = get_upload_path)

    def __str__(self):
        return self.upload