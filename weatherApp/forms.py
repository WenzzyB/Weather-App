from .models import Citys
from django.forms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        model = Citys
        fields = ['name']
        widgets = {'name' : TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Введіть ваше місто'
        })}