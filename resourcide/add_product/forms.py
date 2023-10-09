from django import forms
from .models import Product
from multiupload.fields import MultiFileField

class NameForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter product name', 'class' : 'form__input'}))

class DescriptionForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea(attrs={'class' : 'description-input'}))
    
class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Product  # Specify the model you want to associate with the form
        fields = []  # Define the fields you want to include, or leave it empty to include all fields

    images = MultiFileField(min_num=1, max_num=10, max_file_size=1024 * 1024 * 5)