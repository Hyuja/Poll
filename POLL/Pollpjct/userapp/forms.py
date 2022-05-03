from django.forms import ModelForm
from .models import *

class FileUploadForm(ModelForm):
    class Meta:
        model = logineduserpic
        fields = ['title', 'imgfile']