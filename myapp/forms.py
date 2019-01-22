from django.forms import ModelForm
from .models import Name, File

class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = ('firstName', 'lastName')

    class Meta:
        model = File
        fields = ('upload',)     
 