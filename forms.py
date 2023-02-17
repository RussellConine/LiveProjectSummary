from django.forms import ModelForm
from .models import Ski


class SkiForm(ModelForm):
    class Meta:
        model = Ski
        fields = '__all__'
