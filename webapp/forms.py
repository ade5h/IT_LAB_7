from django.forms import ModelForm
from .models import Works

class WorksForm(ModelForm):
   class Meta:
       model = Works
       fields = '__all__'